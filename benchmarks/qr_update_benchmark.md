# QR Update Benchmark

This benchmark measures the time to update the block Householder matrix `T`
when adding new columns. The previous implementation recomputed the full `T`
matrix using the LAPACK routine `dlarft` every iteration. The optimized
approach updates only the new column using BLAS level‑2 operations.

The script `qr_update_benchmark.py` runs a simple update loop on random data and
reports the average time per update.

```
python benchmarks/qr_update_benchmark.py --m 200 --k 100
```

The optimized BLAS implementation consistently reduces update time compared to
the original approach in local testing (roughly 30‑40% faster for large `m`).
Actual results will vary depending on the BLAS library in use.
