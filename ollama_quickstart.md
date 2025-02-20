# Ollama

<style>
  h1 {
    counter-reset: h2
  }
  h2 {
    counter-reset: h3
  }
  h3 {
    counter-reset: h4
  }
  h2:before {
    counter-increment: h2;
    content: counter(h2) ". "
  }
  h3:before {
    counter-increment: h3;
    content: counter(h2) "." counter(h3) ". "
  }
</style>

[TOC]

## Install on Linux

```sh
    curl -fsSL https://ollama.com/install.sh | sh
```

<br>

## Run DeepSeek-R1

### DeepSeek-R1

```sh
    ollama run deepseek-r1:671b
```

<br>

### DeepSeek-R1-Distill-Qwen-1.5B

```sh
    ollama run deepseek-r1:1.5b
```

<br>

### DeepSeek-R1-Distill-Qwen-7B

```sh
    ollama run deepseek-r1:7b
```

<br>

### DeepSeek-R1-Distill-Llama-8B

```sh
    ollama run deepseek-r1:8b
```

<br>

### DeepSeek-R1-Distill-Qwen-14B

```sh
    ollama run deepseek-r1:14b
```

<br>

### DeepSeek-R1-Distill-Qwen-32B

```sh
    ollama run deepseek-r1:32b
```

<br>

### DeepSeek-R1-Distill-Llama-70B

```sh
    ollama run deepseek-r1:70b
```

<br>

## Remote Service

+ Edit `/systemd/system/ollama.service`:

```ini
    [Service]
    Environment="OLLAMA_HOST=0.0.0.0"
```

+ Restart

```sh
    systemctl restart ollama
```

<br>