# Copyright (c) Meta Platforms, Inc. and affiliates. All Rights Reserved.
import dpf

for N in [1048576, 1048576 * 4, 1048576 * 16]:
    dpf.test_gpu_dpf_perf(N=N, prf=dpf.DPF.PRF_AES128, entrysize=2)
    dpf.test_gpu_dpf_perf(N=N, prf=dpf.DPF.PRF_SALSA20, entrysize=2)
    dpf.test_gpu_dpf_perf(N=N, prf=dpf.DPF.PRF_CHACHA20, entrysize=2)
