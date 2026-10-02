# Coding guidelines

This is a learning project.

The goal is not only to build the application,
but to keep the code understandable.

## General rules

- Prefer simple Python.
- Do not introduce abstractions without a concrete need.
- Do not use design patterns just because they exist.
- Prefer functions over classes when appropriate.
- Avoid unnecessary inheritance.
- Avoid unnecessary dependency injection.
- Avoid premature optimization.
- Keep functions small.
- Use descriptive names.
- Prefer explicit code over clever code.
- Do not add dependencies unless necessary.
- Do not restructure unrelated code.

## Architecture

Start with the simplest possible architecture.

Before creating a new:
- layer
- class
- interface
- repository
- factory
- abstraction

explain what concrete problem it solves.

## Changes

For every task:

1. Explain what needs to change.
2. Propose the smallest solution.
3. Implement it.
4. Explain the resulting request/data flow.
5. Explain anything a junior developer might not understand.

The developer studying this repository should
be able to explain every important line of code.