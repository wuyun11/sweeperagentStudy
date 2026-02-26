# Agent 智能体项目案例

基于 LangChain 的智能体示例项目，包含 RAG、向量存储与 React Agent 等模块。

## 环境要求

- Python 3.x
- 依赖见项目 `requirements.txt`（如有）或根据代码安装相应包

## 启动前必读

### 1. 配置环境变量（二选一）

项目依赖环境变量（如 API Key 等），可通过以下任一方式提供：

- **方式 A（推荐）：项目根目录的 `.env` 文件**
  - 在项目根目录（与 `agent_app`、`config` 同级）创建或编辑 `.env`
  - 按实际使用的服务填入所需变量，例如：使用阿里云百炼/通义时配置 `DASHSCOPE_API_KEY` 等
  - `.env` 已被加入 `.gitignore`，不会提交到仓库，请注意本地妥善配置与保管。
- **方式 B：系统环境变量**  
  不使用 `.env` 也可以，将所需变量配置到本机系统环境变量中即可。

> **注意（使用 Cursor 时建议用 `.env`）**  
> 若把模型 API 等配置在**电脑系统环境变量**中，Cursor 启动时会读取这些变量。一旦该 API 过期或不可用，可能导致 Cursor 后台某些服务启动失败，进而导致 Agent 无法使用——**即使你没有在 Cursor 里配置自定义模型**。因此若同时使用 Cursor 与本项目，更建议用项目内的 `.env` + EnvFile 方式，避免影响 Cursor 自身运行。

### 2. 安装并配置 EnvFile 插件（仅当使用 `.env` 且在 IDE 中运行时需要）

若采用**方式 A（.env）**，并在 **PyCharm** 或 **IntelliJ IDEA** 中通过运行配置启动本项目，需要：

1. **安装 EnvFile 插件**
   - 打开：**File → Settings → Plugins**（Windows/Linux）或 **IntelliJ IDEA → Preferences → Plugins**（macOS）
   - 搜索 **EnvFile**
   - 安装 **EnvFile** 插件（作者一般为 Ashald 等），安装后重启 IDE

2. **在运行配置中启用并指定 `.env`**
   - 打开：**Run → Edit Configurations**
   - 选择或新建用于运行本项目的 Python 运行配置（如 `react_agent`、`rag_service` 等）
   - 在配置界面中找到 **EnvFile** 相关区域，勾选 **Enable EnvFile**
   - 在文件列表中添加项目根目录下的 **`.env`** 文件（路径为 `.env` 或 `$PROJECT_DIR$/.env`）
   - 保存配置

未安装 EnvFile 或未在运行配置中指定 `.env` 时，IDE 启动的进程将无法加载 `.env` 中的变量，可能导致运行报错或无法连接服务。

## 启动项目

- **在 IDE 中**：若用 `.env`，按上述步骤配置好 `.env` 和 EnvFile 后运行对应 Python 运行配置（如 `react_agent`）；若用系统环境变量，无需 EnvFile，直接运行即可。
- **在终端中**：若用 `.env`，请确保当前环境能加载到 `.env`（如项目内使用 python-dotenv 或脚本里 source）；若用系统环境变量，直接执行即可。

完成对应配置后即可正常启动项目。
