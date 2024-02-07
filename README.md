# 功能以功能逻辑顺序：

1.先判断是否需要升级，如果需要则自动升级
2.自动按照填的次数喂猫
3.自动按照填的次数清洗猫
4.根据填写的别的猫的ID，自动发送lay请求
5.自动查是否有需要接收邀请的play请求，如果有的话，就直接接收邀请。


# 安装依赖：

在使用之前，请确保已安装所需的依赖。在命令行中执行以下命令：

```bash
pip install -r requirements.txt
```

# 用户参数配置：

要配置您的 `user_parameters.csv`，请按照以下说明操作：
1. 打开 `user_parameters.csv` 文件。
2. 为每一行填入以下信息：
   - **私钥（Private Key）：** 您的私钥。
   - **猫的ID（myID）：** 您猫的ID。
   - **喂食次数（Feed）：** 填入 7 表示每天喂食7次。
   - **清理次数（Clean）：** 填入 2 表示每天清理2次。
   - **需要发送play申请的别人的猫的id（friendID）：** 不同id之间使用英文逗号隔开，如112233,445566,778899。如果不需要发送play请求则输入为0，不可空置。

每一行代表一个猫的任务序列。任务按顺序执行，每个任务之间有1分钟的冷却时间。

# 补充：

刚开始没看到代理合约开源了，以为没开源，就爬了一些数据，用十六进制写了，写完才发现合约有ABI。不过也能用，就不改了。
