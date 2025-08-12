# mydevenv-checklist

## Installs

### First Priority

- [ ] [iTerm2](https://iterm2.com/)
    - [ ] [fzf](https://github.com/junegunn/fzf)
    - [ ] [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [ ] [Homebrew](https://brew.sh/)

### Language

- [ ] Python(brew)
    - [ ] [uv](https://docs.astral.sh/uv/)
    - [ ] [ruff](https://docs.astral.sh/ruff/installation/)
- [ ] [Elixir (w/ erlang)](https://elixir-lang.org/install.html#macos)
- [ ] [Rust](https://www.rust-lang.org/tools/install)
- [ ] [Go](https://go.dev/doc/install)
- [ ] Node.js(brew)
- [ ] Java
- [ ] Kotlin
- [ ] Flutter (w/ Dart. brew)

### Editor, IDE

- [ ] [Android Studio](https://developer.android.com/studio)
- [ ] [Cursor](https://www.cursor.com/)
- [ ] [Visual Studio Code](https://code.visualstudio.com/)

### Infra

- [ ] [aws-cli](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html)
- [ ] git
    ```bash
    git config --global user.name "jujumilk3"
    git config --global user.email "jujumilk3@gmail.com"
    ssh-keygen -t ed25519 -C "jujumilk3@gmail.com"
    # Enter 3번 (기본 위치, 패스워드 없이)
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    cat ~/.ssh/id_ed25519.pub
    # 또는
    pbcopy < ~/.ssh/id_ed25519.pub  # 클립보드에 복사
    ```
    GitHub → Settings → SSH and GPG keys
    New SSH key 클릭
    복사한 공개키 붙여넣기
- [ ] Docker
    - [ ] [Docker Desktop](https://www.docker.com/get-started/)
- [ ] kubernetes
    - [ ] [kind](https://kind.sigs.k8s.io/)
    - [ ] [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos) - `brew install kubectl`
    - [ ] [kustomize](https://kustomize.io/) - `brew install kustomize`
    - [ ] [minikube](https://minikube.sigs.k8s.io/docs/start/)
    - [ ] [helm](https://helm.sh/) - `brew install helm`

### DB

- [ ] InfluxDB 2+ (brew)
- [ ] MongoDB
- [ ] PostgreSQL
    - [ ] [Postgres.app](https://postgresapp.com/)
- [ ] Redis (brew)

### Browser

- [ ] [Chrome](https://www.google.com/chrome/)
- [ ] [Edge](https://www.microsoft.com/en-us/edge)
- [ ] [Firefox](https://www.mozilla.org/en-US/firefox/new/)

### Tools

- [ ] [AnotherRedisDesktopManager](https://github.com/qishibo/AnotherRedisDesktopManager)
- [ ] [Bruno](https://www.usebruno.com/)
- [ ] [ChatGPT](https://chatgpt.com/download)
- [ ] [Claude](https://www.anthropic.com/claude)
- [ ] [Claude Code](https://www.anthropic.com/claude-code)
- [ ] [Cyberduck](https://cyberduck.io/)
- [ ] [DBeaver](https://dbeaver.io/)
- [ ] [Discord](https://discord.com/download)
- [ ] [Figma](https://www.figma.com/ko-kr/downloads/)
- [ ] [Kubernetes Lens](https://k8slens.dev/)
    - [ ] [Kubernetes Open Lens](https://github.com/MuhammedKalkan/OpenLens)
- [ ] [MongoDB Compass](https://www.mongodb.com/products/compass)
- [ ] [Notion](https://www.notion.so/ko-kr/desktop)
- [ ] [Obsidian](https://obsidian.md/)
- [ ] [Proxyman](https://proxyman.io/)
- [ ] [Raycast](https://raycast.com/)
- [ ] [Redis](https://redis.com/redis-enterprise/redis-insight/)
- [ ] [RunCat](https://kyome.io/runcat/index.html?lang=en)
- [ ] [SnippetsLab](https://www.renfei.org/snippets-lab/)
- [ ] [Typora](https://typora.io/)
- [ ] [WindowTidy](https://www.lightpillar.com/window-tidy.html)

### MCP

- [ ] [playwright-mcp](https://github.com/microsoft/playwright-mcp)

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
```

### vim

```shell
# ~/.vimrc
colo desert
syntax on
```
