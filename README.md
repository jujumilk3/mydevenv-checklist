# mydevenv-checklist

## Installs

### First Priority

- [ ] [iTerm2](https://iterm2.com/)
    - [ ] [fzf](https://github.com/junegunn/fzf)
    - [ ] [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [ ] [Homebrew](https://brew.sh/)
- [ ] [ClaudeCode](https://www.anthropic.com/claude-code)
    - [ ] [playwright-mcp](https://github.com/microsoft/playwright-mcp)

### Language Interpreter, Compiler

- [ ] Python
    - [ ] [uv](https://docs.astral.sh/uv/)
    - [ ] [ruff](https://github.com/astral-sh/ruff)
- [ ] Elixir (w/ erlang)
- [ ] Rust
- [ ] Go
- [ ] Node.js

### Editor, IDE

- [ ] [Cursor](https://www.cursor.com/)
- [ ] [Visual Studio Code](https://code.visualstudio.com/)

### Infra

- [ ] aws-cli
- [ ] git
- [ ] Docker
    - [ ] [Docker Desktop](https://www.docker.com/get-started/)
- [ ] kubernetes
    - [ ] [kind](https://kind.sigs.k8s.io/)
    - [ ] [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos)
    - [ ] [kustomize](https://kustomize.io/)
    - [ ] [minikube](https://minikube.sigs.k8s.io/docs/start/)
    - [ ] [helm](https://helm.sh/)

### DB

- [ ] InfluxDB 2+
- [ ] MongoDB
- [ ] PostgreSQL
    - [ ] [Postgres.app](https://postgresapp.com/)
- [ ] Redis

### Tools

- [ ] [AnotherRedisDesktopManager](https://github.com/qishibo/AnotherRedisDesktopManager)
- [ ] [Bruno](https://www.usebruno.com/)
- [ ] [Cyberduck](https://cyberduck.io/)
- [ ] [DBeaver](https://dbeaver.io/)
- [ ] [Figma](https://www.figma.com/)
- [ ] [Kubernetes Lens](https://k8slens.dev/)
    - [ ] [Kubernetes Open Lens](https://github.com/MuhammedKalkan/OpenLens)
- [ ] [MongoDB Compass](https://www.mongodb.com/products/compass)
- [ ] [Notion](https://www.notion.so/ko-kr/desktop)
- [ ] [Proxyman](https://proxyman.io/)
- [ ] [Raycast](https://raycast.com/)
- [ ] [Redis](https://redis.com/redis-enterprise/redis-insight/)
- [ ] [RunCat](https://kyome.io/runcat/index.html?lang=en)
- [ ] [SnippetsLab](https://www.renfei.org/snippets-lab/)
- [ ] [Typora](https://typora.io/)
- [ ] [WindowTidy](https://www.lightpillar.com/window-tidy.html)

## Profile settings

### zshell

```shell
# ~/.zshrc or ~/.zprofile
HISTFILESIZE=10000000
HISTSIZE=10000000
SAVEHIST=10000000
export CLICOLOR=1
export LSCOLORS=ExGxBxDxCxEgEdxbxgxcxd
export HOMEBREW_NO_AUTO_UPDATE=1
alias k="kubectl"

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
```

#### vim

```shell
# ~/.vimrc
colo desert
syntax on
```
