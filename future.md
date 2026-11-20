# STAC Tasks: Architectural Review & Systems Engineering Roadmap (future.md)

---

## 1. Architectural Code Review & Current State Analysis

STAC Tasks represents a comprehensive, multi-disciplinary engineering portfolio spanning software systems development (POSIX Shell automation, Python Rich CLIs, and C vs Rust performance benchmarks) and hardware/avionics closed-loop simulation (microcontroller digital I/O, multi-sensor LCD telemetry, and actuator steering dynamics).

### Architectural Strengths
- **Defensive Shell Engineering (`software/Task-01`):** Demonstrates robust shell scripting practices (`segrV2.sh`) by avoiding common pitfalls (handling whitespace in paths, idempotent directory creation via `mkdir -p`, script self-exclusion).
- **Comparative Systems Benchmarking (`software/Task-04`):** Direct algorithmic comparison between C (Clang) and Rust (Cargo) across Project Euler problems, evaluating compiler optimizations, type safety, and memory footprints.
- **Hardware Telemetry Modeling (`hardware/`):** Closed-loop control theory demonstrations recorded in high-definition visual simulation logs for verification.

### Identified Bottlenecks & Modernization Opportunities
1. **Interactive Simulation vs Code-Driven HIL:** Hardware tasks are currently captured as static `.mp4` video recordings rather than executable, reproducible hardware-in-the-loop (HIL) simulation test harnesses.
2. **Bash Portability:** The file organizer relies on GNU-specific coreutils flags that may behave differently on BSD / macOS shells.
3. **Rust Embedded (no_std) Expansion:** Hardware control algorithms are modeled conceptually rather than implemented directly in bare-metal Rust (`no_std`) for embedded microcontrollers.

---

## 2. Strategic Engineering Roadmap

```mermaid
flowchart TD
    subgraph Phase 1: Reproducible Hardware-in-the-Loop Simulation
        P1A[Wokwi / QEMU Virtual Microcontroller Harness] --> P1B[Automated Headless Simulation CI/CD]
        P1B --> P1C[Interactive Web-Based Circuit Canvas]
    end

    subgraph Phase 2: Embedded no_std Rust Firmware
        P2A[STM32 / RP2040 PAC & HAL Implementations] --> P2B[Zero-Cost Real-Time Closed Loop PID]
        P2B --> P2C[RTIC Real-Time Interrupt Controller Suite]
    end

    subgraph Phase 3: Cloud SpatioTemporal Geospatial (STAC) Engine
        P3A[SpatioTemporal Asset Catalog (STAC) Parser] --> P3B[GeoTIFF Satellite Raster Ingestion]
        P3B --> P3C[Automated Remote Sensing NDVI Pipeline]
    end

    subgraph Phase 4: Multi-Sensor Autonomous Flight Controller
        P4A[Extended Kalman Filter Sensor Fusion: IMU + Baro] --> P4B[Actuator Failover Interlocks]
        P4B --> P4C[MAVLink Dynamic Telemetry Teleportation]
    end

    Phase 1 --> Phase 2
    Phase 2 --> Phase 3
    Phase 3 --> Phase 4
```

---

## 3. Detailed Milestone Execution Plan

### Milestone 1: Automated Wokwi / QEMU Simulation Testbed
- [ ] **Headless Hardware Testing:** Replace static MP4 recordings with automated Wokwi CLI integration testing, asserting UART baud outputs and LCD display strings via GitHub Actions.
- [ ] **POSIX Compliant Shell Refactoring:** Ensure `segrV2.sh` passes ShellCheck with zero warnings across both GNU Bash and Dash/Zsh.

### Milestone 2: Bare-Metal `no_std` Rust Firmware Suite
- [ ] **Microcontroller Drivers in Rust:** Implement non-blocking I2C LCD and ultrasonic sensor drivers using `embedded-hal` for RP2040 and STM32F4.
- [ ] **Deterministic Interrupt Scheduling:** Utilize Real-Time Interrupt-driven Concurrency (RTIC) to guarantee $<5\mu\text{s}$ jitter on steering actuator PWM signals.

### Milestone 3: Real Earth-Observation STAC (SpatioTemporal Asset Catalog) Integration
- [ ] **STAC Python Processing Engine:** Build a pipeline utilizing `pystac` and `rasterio` to search, download, and index Sentinel-2 and Landsat-9 multispectral imagery.
- [ ] **Cloud-Optimized GeoTIFF (COG) Streaming:** Process multi-band vegetation indices directly from cloud storage buckets with zero disk downloads.

### Milestone 4: Autonomous Avionics & Sensor Fusion Kernel
- [ ] **Extended Kalman Filter (EKF):** Fuse noisy 6-DOF IMU accelerometer/gyroscope readings with barometric altitude to maintain accurate real-time state vectors.
- [ ] **Automated MAVLink Telemetry:** Transmit live pitch, roll, yaw, and battery health telemetry over simulated radio links.
