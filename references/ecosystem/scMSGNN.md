# scMSGNN — 0.3.0

> 数据源：github.com/YuLab-SMU/scMSGNN@devel
> 4 个已知符号

## Generic (4)

- `ensure_tensor(x, dtype=torch::torch_float32(), device=NULL, ...)`
- `scMSGNN_Annotate(object, markers, assay=NULL, n_background=100, slot="data", ...)`
- `scMSGNN_CorrectBatch(object, features=NULL, k_neighbors=20, k_scales=NULL, sign_k=2, hidden_dims=c(128, 64), epochs=50, lr=0.001, batch_size=256, device="cpu", adj_matrix=NULL, pathway_mask=NULL, adj_lambda=1.0, batch=NULL, batch_lambda=1.0, ...)`
- `scMSGNN_Run(object, features=NULL, k_neighbors=20, k_scales=NULL, sign_k=2, hidden_dims=c(128, 64), epochs=50, lr=0.001, batch_size=256, device="cpu", adj_matrix=NULL, pathway_mask=NULL, adj_lambda=1.0, ...)`
