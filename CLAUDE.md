# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Streamlit-based interactive course presentation app for "AI 領航員計畫" (AI Navigator Program) — a 21-day hardware automation transformation course. The app serves as both teaching material and a live demo, featuring a photo booth (拍貼機) prototype simulator.

The UI is entirely in Traditional Chinese (繁體中文).

## Running the App

```bash
streamlit run course_app.py
```

Requires: `streamlit` (Python package). No other dependencies.

## Architecture

Single-file app (`course_app.py`) with four sections controlled via sidebar radio navigation:

1. **Section 0** — Course vision/intro
2. **Section 1** — Vibe Coding concepts (tabbed layout)
3. **Section 2** — Permissions & deployment guidelines (expandable sections)
4. **Section 3** — Photo booth prototype with stateful multi-stage flow (payment → shooting → printing), using `st.session_state` for stage and photo count management

Custom CSS is injected via `st.markdown` with `unsafe_allow_html=True` for slide-style formatting.
