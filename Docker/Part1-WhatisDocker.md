## 🧩 Part 1 – What is Docker

### 🔹 The Problem We’re Trying to Solve

As software developers, we build applications that millions of users depend on.
We write code, connect to databases, test features, and configure multiple services — all on our own local machines.

But when we share this project with teammates (developers, testers, or DevOps engineers), things often break.
Why? Because each system needs to be configured again from scratch.
If even one dependency version or OS-level setting differs, the application may fail to run.
What works on your laptop might not work in production.

To solve this problem **before containers**, we used **virtualization**.

---

### 🔹 What is Virtualization?

Virtualization introduced the idea of running multiple operating systems (OS) on a single physical machine.
It consists of three layers:

**Application → OS → Hardware**

And inside a virtualized setup:

* **Guest OS** – the secondary OS (like Ubuntu or Windows Server) running inside the host.
* **Hypervisor** – software that manages and isolates the guest OSs.
* **Host OS + Hardware** – the real computer underneath.

So, in virtualization you could run two operating systems at once.
Your application runs on the **guest OS**, which runs on the **hypervisor**, which finally talks to the **host OS**.

You could even send that guest OS image to another team — they could copy and run it on their hypervisor.

However, to keep applications isolated, we often used multiple guest OS instances on the same server.
Each of these consumed a lot of **CPU and RAM**, even if we just wanted to run a single small app.
This made virtualization heavy and inefficient.

---

### 🔹 From Virtualization to Containerization

**Containerization** solved this.
Instead of giving every app its own guest OS, we let multiple apps share the same OS kernel but run in isolated spaces called **containers**.

A container can package everything an app needs — compilers, web servers, databases, and configurations — into one environment.
We simply give the container to any team, and it will run exactly the same everywhere.

**Benefits:**

* ✅ Isolation: Each container runs in its own isolated environment with its own filesystem, network, and dependencies. This ensures that one app’s configuration or bug doesn’t interfere with another’s.

* ⚡ Lightweight (no extra OS needed): Containers share the same operating system kernel instead of running full guest OSs like in virtualization. This drastically reduces memory and CPU usage, allowing you to run many containers on the same machine.

* 🚀 Fast startup: Since containers don’t need to boot an entire OS, they start within seconds. This helps scale systems quickly and makes development cycles faster.

* 🔐 Secure: Containers are isolated from each other and from the host system. Even if one container is compromised, the rest remain safe, reducing security risks.

* 🌍 Portable across environments: A container includes all dependencies, libraries, and configurations. The same container runs identically on any system — local, testing, or production — removing the “it works on my machine” problem.

* 📈 Scalable — you can spin up multiple identical containers easily

But how do we actually create and manage these containers?
That’s where **Docker** comes in.

---

### 🔹 What is Docker?

**Docker** is a platform that lets us **package, distribute, and run** applications inside containers.

A **container** is a lightweight, isolated environment that includes an application along with all its dependencies, libraries, and configurations.
Because everything is self-contained, the same container runs consistently on any machine — whether on a laptop, testing server, or production cloud.

Before containers, every environment required separate installation and configuration for each service, often leading to dependency conflicts.
With Docker, the entire environment is defined once, and we only need one command to start it.
The only requirement on any system is the **Docker runtime** — which executes containers.

---

### 🔹 Where Containers Live

Containers are stored and shared through **container repositories** (registries).
They can be:

* **Public** — e.g. [Docker Hub](https://hub.docker.com)
* **Private** — internal company registries

Example:

```bash
docker run postgres:9.6
```

If the PostgreSQL 9.6 image isn’t already on your machine, Docker automatically downloads it from Docker Hub.

---

### 🔹 Images and Layers

A **Docker image** is a read-only **blueprint** that defines everything needed to run an app.
Images are made up of multiple **layers**, each representing a change (like installing dependencies or adding files).

If you later pull another version (say `postgres:10`), Docker downloads only the new or different layers — saving both space and bandwidth.

---

### 🔹 Containers vs Images

| Concept       | Meaning                                                            |
| ------------- | ------------------------------------------------------------------ |
| **Image**     | The blueprint / artifact — defines what will run.                  |
| **Container** | A running instance of that image — the live, isolated environment. |

To view all active containers:

```bash
docker ps
```

Example output:

```
CONTAINER ID   IMAGE        COMMAND               STATUS          PORTS
fad0f8456ca7   postgres:9.6 "docker-entrypoint…"  Up 47 seconds   5432/tcp
```

Here, container `fad0f8456ca7` is actively running PostgreSQL 9.6 on port 5432.

---

### 🔹 Docker Hub and Images

**Docker Hub** acts like a cloud storage for container images.
It hosts images of most popular servers, databases, and tools — ready to pull and run.
You can also upload (push) your own images.

To create your own image, you write a **Dockerfile**, which defines:

* The base image
* Commands to install dependencies
* Environment setup

Then you build it with:

```bash
docker build -t myapp:latest .
```

---

### 🔹 Storage and Compose

* **Docker Volumes** — persistent storage to save data outside containers.
* **Docker Compose** — a tool to run multi-container applications (e.g. web + db + cache) with a single YAML file.

---

### 🧠 Key Idea

Think of a **Docker image** as a **recipe**, and a **container** as the **dish** prepared from that recipe.
You can cook (run) as many dishes (containers) as you like from the same recipe (image), anywhere, anytime — and they’ll all taste exactly the same.
