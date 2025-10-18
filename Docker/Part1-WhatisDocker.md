## Part 1 – What is Docker

**Docker** is a platform that lets us package, distribute, and run applications inside **containers**.

A **container** is a lightweight, isolated environment that bundles an application along with all its required dependencies, libraries, and configurations into a single portable unit. Because everything the app needs is packaged inside, the same container can run consistently on any system — whether it’s a developer’s laptop, a testing server, or production cloud. This makes development and deployment much faster and more reliable.

Before containers, each machine required separate installation and configuration for every service. The setup steps often varied by operating system, causing dependency conflicts, manual errors, and wasted time.

With containers, the entire environment is pre-configured once, so we only need one command to start the app. The only requirement on the target system is the **Docker runtime**, which executes the container.

---

### 🔹 Where Containers Live

Containers are stored and shared via **container repositories** — special registries for container images.
They can be:

* **Public** (e.g. Docker Hub)
* **Private** (for internal or enterprise use)

For example, when we run:

```bash
docker run postgres:9.6
```

Docker automatically pulls the **PostgreSQL 9.6** image from **Docker Hub** if it isn’t already downloaded.

---

### 🔹 Images and Layers

A **Docker image** is a read-only package — the blueprint that contains everything needed to run the app.
Images are built from multiple **layers**, where each layer represents changes (like adding dependencies or files).
If you later pull another version (say `postgres:10`), Docker will only download the layers that differ — saving space and bandwidth.

---

### 🔹 Containers vs Images

| Concept       | Meaning                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------- |
| **Image**     | The blueprint or artifact — defines what to run.                                                   |
| **Container** | A running instance created from an image — the actual isolated environment where the app executes. |

You can list all currently running containers with:

```bash
docker ps
```

Output will show:

* **CONTAINER ID** – unique identifier
* **IMAGE** – which image the container is based on
* **STATUS** – how long it’s been running
* **PORTS** – network ports exposed

Example (from your screenshot):

```
CONTAINER ID   IMAGE        COMMAND               STATUS          PORTS
fad0f8456ca7   postgres:9.6 "docker-entrypoint…"  Up 47 seconds   5432/tcp
```

This means a container (ID `fad0f8456ca7`) is actively running a PostgreSQL 9.6 instance on port 5432.

---

### 🧠 Key Idea

Think of a **Docker image** as a recipe, and a **container** as the actual dish prepared from that recipe.
You can create many identical dishes (containers) from the same recipe (image) anywhere, anytime, with the same results.

---

Would you like me to frame **Part 2 – Docker Architecture (Engine, Image, Container, Registry)** next so your notes naturally continue from here?
