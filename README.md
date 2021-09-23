# Uniswap V2
  
- [Uniswap V2](#uniswap-v2)
  - [1. Introduction](#1-introduction)
  - [2. Get the Source Code](#2-get-the-source-code)
    - [2.1 Create A Directory](#21-create-a-directory)
    - [2.2 Check out Uniswap v2 Core](#22-check-out-uniswap-v2-core)
    - [2.3 Check out Uniswap v2 Periphery](#23-check-out-uniswap-v2-periphery)
  - [3. Install Yarn](#3-install-yarn)
    - [3.1 Enable the Official Yarn Repository](#31-enable-the-official-yarn-repository)
    - [3.2. Install Yarn](#32-install-yarn)
  - [4. Compile Uniswap Source Code](#4-compile-uniswap-source-code)
    - [4.1 Install Yarn Dependencies](#41-install-yarn-dependencies)
    - [4.2. Compile Core](#42-compile-core)
    - [4.3. Compile Periphery](#43-compile-periphery)
    - [4.4. Check Files](#44-check-files)
    - [4.4. Copy the Files to the Client Docker](#44-copy-the-files-to-the-client-docker)
  - [5. Testnet Interaction](#5-testnet-interaction)
  - [5. Contract Deployment](#5-contract-deployment)
    - [5.1. Deploy the Uniswap v2](#51-deploy-the-uniswap-v2)
  - [5. Call Uniswap v2](#5-call-uniswap-v2)
    - [5.1. Mint](#51-mint)
    - [5.2. Approve](#52-approve)
    - [5.3. liquidity Pool](#53-liquidity-pool)
    - [5.4. Swap](#54-swap)

## 1. Introduction

This document shows you how to compile, deploy and run [Uniswap V2](https://github.com/Uniswap) on an Arcology testnet.If you are only interested in trying Arcology testnet out without diving into specific technical details, then **[please check this document out for an easy start.](./uniswap-v2-test-scripts.md)**

## 2. Get the Source Code

---

### 2.1 Create A Directory

```sh
> mkdir tmp
```

### 2.2 Check out Uniswap v2 Core

```sh
> git clone https://github.com/Uniswap/uniswap-v2-core
```

### 2.3 Check out Uniswap v2 Periphery

```sh
> git clone https://github.com/Uniswap/uniswap-v2-periphery
```

## 3. Install Yarn

---
Yarn is a node.js package manager, please go to https://classic.yarnpkg.com/lang/en/ for more info.

### 3.1 Enable the Official Yarn Repository

```sh
> curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
> echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

### 3.2. Install Yarn

Update the package list, and then install Yarn.

```sh
> sudo apt update
> sudo apt install yarn
```

## 4. Compile Uniswap Source Code

---

### 4.1 Install Yarn Dependencies

Installing all the dependencies of project

``` sh
> yarn
```

### 4.2. Compile Core

Under the uniswap core directory directory  

```sh
> yarn compile
```

![alt text](./img/yarn-core-compile.png)

### 4.3. Compile Periphery

Under the uniswap periphery directory directory  

```sh
> yarn compile
```

![alt text](./img/yarn-periphery-compile.png)

### 4.4. Check Files

Making sure the following files exist

```sh
> ls -l tmp/uniswap-v2-core/build/UniswapV2Factory.json
> ls -l tmp/uniswap-v2-periphery/build/UniswapV2Router02.json
```

### 4.4. Copy the Files to the Client Docker

The next step is to copy the files to an Arcology docker container. Which containers all the client tools, libraries and packages that users will need in order to interact with an Arcology node. The client docker is listen on port 32768 for incoming connections.

You need to copy the compiled contracts into the container, so they can be deployed on the testnet.

```sh
> scp tmp/uniswap-v2-core/build/UniswapV2Factory.json s9-hpis-monaco-testnet@192.168.1.109:/home/txs
> scp tmp/uniswap-v2-core/build/UniswapV2Router02.json s9-hpis-monaco-testnet@192.168.1.109:/home/txs
```

## 5. Testnet Interaction

---
You can interact with the Arcology testnet through HTTP connections right now. Arcology provides a collection of tools and libraries to facilitate the process. These tools are included in the docker container that comes with the installer package. You don't need to do anything as the installer will automatically set up everything for you.

Once the installation is successfully complete, there should be a docker container listening on port `32768` of the host machine an Arcology node is running.

## 5. Contract Deployment

You have to deploy the uniswap contracts on the Arcology testnet first between calling them.

### 5.1. Deploy the Uniswap v2

If the Host IP address is https://192.168.1.109:8080, then in the client docker container, run the following command under the root direct to deploy the contracts to the testnet. The port 8080 is reserved for communications with clients.

```sh
> cd uniswap
> sh deploy.sh http://192.168.1.109:8080 ../data/uniswap_v2/UniswapV2Factory.json ../data/uniswap_v2/UniswapV2Router02.json
```

You should be able to see the screen below if the deployment is successfuly completed.

![alt text](./img/uniswap-deployment.png)

## 5. Call Uniswap v2

The package comes with some pre-genearted transactions files ready to used.

### 5.1. Mint

Mint the first token

```sh
> python sendtxs.py http://192.168.1.109:8080 ./data/uniswap_v2/token1_mint_200.out
```

![alt text](./img/uniswap-token1-mint-200.png)

Mint the second token

```sh
> python sendtxs.py http://192.168.1.109:8080 ./data/uniswap_v2/token2_mint_200.out
```

![alt text](./img/uniswap-token2-mint-200.png)

### 5.2. Approve

Approve the first token

```sh
> python sendtxs.py http://192.168.1.109:8080 ./data/uniswap_v2/token1_approve_200.out
```

Approve the second token

```sh
> python sendtxs.py http://192.168.1.109:8080 ./data/uniswap_v2/token2_approve_200.out
```

### 5.3. liquidity Pool

Add some liquidity to the pool

```sh
> python sendtxs.py http://192.168.1.109:8080 ./data/uniswap_v2/add_liquidity_200.out
```

### 5.4. Swap

Swap between two types of tokens

```sh
> python sendtxs.py http://192.168.1.109:8080 ./data/uniswap_v2/swap_200.out
```