# 🤖 Agno AI Multi-Agent CI/CD

A production-style **multi-agent AI system** built with **Agno**, integrated with **GitHub Actions, Docker, Docker Hub, and AWS EC2** to demonstrate a complete end-to-end **CI/CD pipeline**.

The system uses multiple specialized AI agents to research, analyze, and generate structured answers for a given topic.

---

## 🚀 Project Overview

This project demonstrates how an AI application can be developed, tested, containerized, and automatically deployed using modern DevOps practices.

The AI system consists of three specialized agents:

- 🔎 **Researcher Agent** — Researches the given topic
- 📊 **Analyst Agent** — Analyzes the research and extracts insights
- ✍️ **Writer Agent** — Generates the final structured response

An **Agno Team** coordinates these agents and manages the workflow.

---

## 🏗️ Architecture

```text
                    Developer
                       │
                       │ git push
                       ▼
                  GitHub Repository
                       │
                       ▼
                GitHub Actions
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     Run Pytest              Build Docker Image
          │                         │
          ▼                         ▼
    Test Report                 Docker Hub
                                    │
                                    │ docker pull
                                    ▼
                              AWS EC2 Instance
                                    │
                                    ▼
                              Docker Container
                                    │
                                    ▼
                              Agno AI Team
                         ┌──────────┼──────────┐
                         ▼          ▼          ▼
                    Researcher  Analyst    Writer