# Empowering IoT Networks with Open-Source SDN using Multi-Tenant Slicing with Microservice-Based Ryu Controller

## Research Objectives and Goals

This research aims to:

- Understand how a microservice-based SDN Controller architecture operates.
- Explore the principles and implementation of Network Slicing in IoT networks.
- Develop an effective multi-tenant SDN Controller system based on microservices using the Ryu framework.
- Evaluate the impact of microservice-based SDN Controller on network slicing performance in IoT environments.
- Design and implement a scalable, modular SDN controller for multi-tenant slicing applicable to IoT use cases.

## Research Overview

In this study, the Ryu SDN Controller is decomposed into microservices, breaking down monolithic components into independent services managed via Docker containers and orchestrated with Kubernetes. This design enables flexible, scalable multi-tenant network slicing tailored for IoT deployments.

The Flow Space feature from the Flowvisor controller container is leveraged to enforce tenant isolation and slice management on the data plane.

## Network Slicing Specification

The slicing scenario is based on IoT device groups with distinct service requirements and bandwidth allocations, such as:

| Service Type          | Slice Name     | Bandwidth Allocation | Network Path          |
| --------------------- | -------------- | -------------------- | --------------------- |
| Environmental Sensors | Sensor Slice   | 1 Mbps               | IoT Devices Gateway   |
| Surveillance Cameras  | Video Slice    | 5 Mbps               | Video Processing Unit |
| Smart Meters          | Meter Slice    | 500 Kbps             | Meter Aggregator      |
| Emergency Alerts      | Critical Slice | 2 Mbps               | Control Center        |

## Experimental Testbed

The research setup consists of multiple virtualized environments running on OpenStack, simulating the IoT network slices and controller microservices.

| VM Name   | OS Version   | Specs                   | IP Addresses             |
| --------- | ------------ | ----------------------- | ------------------------ |
| Master    | Ubuntu 20.04 | 4 vCPU, 4 GB RAM, 30 GB | 10.0.0.241, 172.20.3.237 |
| Worker 1  | Ubuntu 20.04 | 8 vCPU, 4 GB RAM, 50 GB | 10.0.2.207, 172.20.3.178 |
| Worker 2  | Ubuntu 20.04 | 4 vCPU, 4 GB RAM, 30 GB | 10.0.0.128, 172.20.3.242 |
| Flowvisor | Ubuntu 14.04 | 2 vCPU, 2 GB RAM, 20 GB | 10.0.1.242, 172.20.0.119 |

## Key Components and Tools

- **Ryu SDN Controller**: Microservice-based controller framework for programmable network management.
- **Flowvisor**: OpenFlow network virtualization layer enabling slice isolation.
- **Docker & Kubernetes**: Containerization and orchestration platform for microservices deployment.
- **OpenStack**: Cloud infrastructure for virtual machine provisioning.
- **IoT Device Simulation**: Emulated IoT devices generating traffic according to slice requirements.

## Getting Started

### Prerequisites

- Docker & Kubernetes cluster setup
- OpenStack environment for VM management
- Python 3.x with Ryu controller dependencies
- Flowvisor installed and configured

### Installation and Deployment

Instructions for deploying the microservice-based Ryu controller and network slicing environment will be provided here.

## Usage and Evaluation

- Launch and manage SDN controller microservices via Kubernetes.
- Deploy Flowvisor to create and manage network slices.
- Simulate IoT traffic for different slices and monitor performance metrics such as throughput, latency, and isolation.
- Analyze the effect of multi-tenant slicing on network performance.

## References

Include key references, papers, and related work relevant to this research.

---


