# Empowering IoT Networks with Open-Source SDN using Multi-Tenant Slicing with Microservice-Based Ryu Controller

The objectives and benefits to be achieved in this research are:
- Understand how a microservice-based SDN Controller architecture operates.
- Explore the principles and implementation of Network Slicing in IoT networks.
- Develop an effective multi-tenant SDN Controller system based on microservices using the Ryu framework.
- Evaluate the impact of microservice-based SDN Controller on network slicing performance in IoT environments.
- Design and implement a scalable, modular SDN controller for multi-tenant slicing applicable to IoT use cases.

## Introduction
Network slicing is a key enabler in 5G and beyond architectures, allowing multiple virtual networks to coexist on a shared physical infrastructure with isolated and customizable resource allocations. This project explores a slicing implementation at the SDN forwarding level using the Ryu controller and Open vSwitch, targeting Everything-as-a-Service (EaaS) scenarios.

Unlike hypervisor-based slicing, this solution employs Linux resource reservation tools (e.g., Cgroups, traffic control) combined with SDN programmability to efficiently allocate CPU, bandwidth, memory, and storage resources to tenant slices.

## Technologies and Tools
- **Ryu SDN Controller:** Python-based SDN controller for managing OpenFlow-enabled switches.
- **Mininet:** Network emulator to simulate the core and tenant network topologies.
- **Open vSwitch (OVS):** Virtual switch supporting OpenFlow and MPLS tunneling.
- **Iperf:** Network traffic generator for performance testing.
- **Linux Cgroups:** Resource
