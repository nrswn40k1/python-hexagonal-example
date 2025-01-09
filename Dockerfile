# ----------------------------------------------------------
# --- ベースステージ ---
FROM python:3.12-slim as base

ARG UID=1000
ARG GID=1000

ENV PATH /root/.local/bin:$PATH

RUN apt-get update && apt-get install -y \
    sudo \
    curl

# User and Group Setup
RUN groupadd -g $GID user \
    && useradd -m -s /bin/bash -u $UID -g $GID user \
    && echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user

# Install Poetry
RUN apt-get update && apt-get install -y \
    && echo "alias poetry='sudo /root/.local/bin/poetry'" >> /home/user/.bash_aliases \
    && curl -sSL https://install.python-poetry.org | POETRY_VERSION=2.0.0 python3 - \
    && poetry config virtualenvs.create false


# ----------------------------------------------------------
# --- 開発用ステージ ---
FROM base as dev
RUN apt-get update && apt-get install -y \
    git \
    bash-completion \
    wget \
    tree

# Install Python packages
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Install Terraform
# RUN apt-get update && sudo apt-get install -y gnupg software-properties-common \
#     && wget -O- https://apt.releases.hashicorp.com/gpg | \
#     gpg --dearmor | \
#     tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null \
#     && gpg --no-default-keyring \
#     --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
#     --fingerprint \
#     && echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
#     https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
#     tee /etc/apt/sources.list.d/hashicorp.list \
#     && apt-get update \
#     && apt-get install terraform -y

# ----------------------------------------------------------
# --- Gcloud上の開発用ステージ ---
# FROM dev as dev-gcloud
# RUN sudo apt-get install -y apt-transport-https ca-certificates gnupg curl \
#     && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
#     && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
#     && apt-get update -y && apt-get install google-cloud-cli -y
