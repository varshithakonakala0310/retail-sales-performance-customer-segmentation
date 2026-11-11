import os, warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
BASE=os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(BASE,"data"),exist_ok=True); os.makedirs(os.path.join(BASE,"results"),exist_ok=True)
rng=np.random.default_rng(42)
customers=800; orders=5000
cust_ids=np.arange(1,customers+1)
order_cust=rng.choice(cust_ids,size=orders,p=[None][0] if False else None)
# simpler uniform choice
order_cust=rng.integers(1,customers+1,size=orders)
dates=pd.to_datetime("2023-01-01")+pd.to_timedelta(rng.integers(0,730,size=orders),unit="D")
qty=rng.integers(1,6,size=orders); price=rng.lognormal(3.2,0.6,size=orders)
df=pd.DataFrame({"order_id":range(1,orders+1),"customer_id":order_cust,"order_date":dates,"quantity":qty,"unit_price":price.round(2)})
df["revenue"]=(df["quantity"]*df["unit_price"]).round(2)
df.to_csv(os.path.join(BASE,"data","retail_orders_synthetic.csv"),index=False)
ref=df["order_date"].max()+pd.Timedelta(days=1)
rfm=df.groupby("customer_id").agg(recency=("order_date",lambda s:(ref-s.max()).days),frequency=("order_id","count"),monetary=("revenue","sum")).reset_index()
scaler=StandardScaler(); X=scaler.fit_transform(rfm[["recency","frequency","monetary"]])
km=KMeans(n_clusters=4,random_state=42,n_init=10); rfm["segment"]=km.fit_predict(X)
rfm.to_csv(os.path.join(BASE,"data","customer_rfm_segments.csv"),index=False)
monthly=df.set_index("order_date").resample("M")["revenue"].sum()
seg=rfm.groupby("segment").agg(customers=("customer_id","count"),avg_monetary=("monetary","mean"),avg_frequency=("frequency","mean"),avg_recency=("recency","mean"))
total_rev=df["revenue"].sum()
with open(os.path.join(BASE,"results","results_summary.txt"),"w") as f:
    f.write("Retail Sales Performance & Customer Segmentation — SYNTHETIC RESULTS\n")
    f.write(f"Orders: {len(df)}, Customers: {customers}, Total revenue: GBP {total_rev:.2f}\n")
    f.write(f"Date range: {df['order_date'].min().date()} to {df['order_date'].max().date()}\n")
    f.write(f"Average order value: GBP {df['revenue'].mean():.2f}\n")
    f.write(f"Peak month revenue: GBP {monthly.max():.2f} in {monthly.idxmax().strftime('%Y-%m')}\n")
    f.write("Segments (KMeans k=4 on RFM):\n")
    for i,r in seg.iterrows(): f.write(f"  Segment {i}: customers={int(r['customers'])} avg_monetary=GBP {r['avg_monetary']:.2f} avg_frequency={r['avg_frequency']:.2f} avg_recency_days={r['avg_recency']:.1f}\n")
    top=seg["avg_monetary"].idxmax(); f.write(f"Highest-value segment: {top} (avg monetary GBP {seg.loc[top,'avg_monetary']:.2f})\n")
print(seg); print(f"total_rev={total_rev:.2f}")
