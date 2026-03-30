一定要用源码去安装habitat，请参考
https://blog.csdn.net/gitblog_00735/article/details/154770062
如果你执行以下操作报错：
python -m habitat_sim.utils.datasets_download \
    --uids habitat_test_scenes \
    --data-path ./data
则使用：
hf download ai-habitat/habitat_test_scenes \
  --repo-type dataset \
  --local-dir data/habitat_test_scenes

数据下载
https://blog.csdn.net/qq_41204464/article/details/149549133