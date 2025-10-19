## 🧩 Part 3 – Docker Architecture

Before getting into the full architecture, let’s first understand the main components of the **Docker Engine** — the core of the Docker platform.

---

### 🔹 What is Docker Engine?

In simple words, **Docker Engine** is the runtime that builds, runs, and manages Docker containers.
It’s the layer responsible for all the actual “container magic” happening behind the scenes.

The stack comprises three core parts (as shown in the first diagram):

1. **Docker Daemon (`dockerd`)**

   * A background process that manages running containers, images, networks, and volumes.
   * It listens for API requests from the client and performs actions such as building images, creating containers, or starting services.
   * It’s responsible for the full container lifecycle.

2. **Docker Engine REST API**

   * The communication bridge between the **client** and the **daemon**.
   * Allows other apps or external systems to interact with Docker programmatically — to create containers, list images, or upload data.
   * Works over HTTP.

3. **Docker CLI (Command-Line Interface)**

   * The user-facing command-line tool.
   * When you run a command like `docker run` or `docker ps`, it sends that request to the daemon through the REST API.
   * Developers primarily interact with Docker through this CLI.

Both **Docker Client** and **Docker Daemon** can run on the same system, but they can also communicate remotely via the REST API if Docker is running on another machine or cloud server.

**Flow summary:**
Client → sends command → Docker Daemon → executes it → manages containers/images/volumes/networks.

---

### 🔹 Docker Architecture Overview

Refer to the second diagram.
Docker’s architecture consists of three main parts:

1. **Docker Client**

   * This is where users interact using commands like:

     ```bash
     docker build
     docker pull
     docker run
     ```
   * The client passes these commands to the Docker Daemon (usually running on the Docker Host).

2. **Docker Host**

   * This machine runs the **Docker Daemon**.
   * It manages all **Docker objects** — such as **images**, **containers**, **networks**, and **volumes**.
   * It performs the heavy lifting: building images, running containers, and maintaining communication.

3. **Docker Registry**

   * A storage space (public or private) for Docker images.
   * The most common example is **Docker Hub** — a public registry that stores millions of images ready to use.
   * You can also create a **private registry** within your organization.

---

### 🔹 Example Workflow

Let’s take `docker run` as an example:

1. You type `docker run postgres:9.6` in your terminal.
2. The **Docker client** sends this command to the **Docker Daemon**.
3. The **Daemon** checks if the image (`postgres:9.6`) is available locally.

   * If not, it **pulls** the image from the **Docker Registry**.
4. The Daemon then **creates a new container** from that image.
5. It allocates a **read-write filesystem** on top of the image layers.
6. It connects the container to the default **Docker network**.
7. Finally, it **starts** the container.

This entire workflow happens automatically once the command is executed.

---

### 🔹 Components of Docker Engine

| Component                     | Description                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------- |
| **Docker Daemon (`dockerd`)** | Manages Docker objects like containers, images, volumes, and networks.                         |
| **Docker Client**             | CLI tool for interacting with Docker. Sends commands via REST API.                             |
| **Docker Engine REST API**    | Enables communication between Docker components and external tools.                            |
| **Docker Images**             | Read-only blueprints that define how a container should be built and run.                      |
| **Docker Containers**         | Running instances of images — actual environments where apps execute.                          |
| **Docker Registry**           | Repository for storing and sharing Docker images (public like Docker Hub or private).          |
| **Docker Volumes**            | Mechanism to persist and share data between containers.                                        |
| **Docker Networking**         | Software-defined networks that let containers communicate with each other or external systems. |
| **Docker Compose**            | Tool for defining and running multi-container applications using a YAML file.                  |

---

### 🔹 Visual Summary

**From the First Diagram (InterviewBit):**

* The **Client** (CLI) communicates with the **Server** (Daemon) via the **REST API**.
* The **Daemon** manages all Docker objects — **containers**, **images**, **volumes**, and **networks**.
* Each of these represents a part of your application setup and lifecycle.

**From the Second Diagram:**

* **Client** → Sends commands like `docker build`, `docker pull`, `docker run`.
* **Docker Host** → Executes these using the Docker Daemon.
* **Registry** → Stores and distributes images used by Docker Host.

---

### 🧠 Why This Architecture Works So Well

* **Separation of concerns:** Client and Daemon separation allows remote management and automation.
* **Portability:** Images can move across any Docker host that runs the same Engine.
* **Scalability:** Multiple containers can run from the same image with minimal overhead.
* **Automation:** REST API allows full automation and integration with CI/CD tools.
* **Flexibility:** Works across environments — local, cloud, or hybrid setups.
