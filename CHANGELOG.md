# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.7.1] - 2024-09-04

### Added
- Add compatibility with jrl-cmakemodules workspace ([#99](https://github.com/Simple-Robotics/proxsuite-nlp/pull/99))

### Fixed
- Remove CMake CMP0167 and CMP0169 warnings ([#100](https://github.com/Simple-Robotics/proxsuite-nlp/pull/100))

## [0.7.0] - 2024-05-14

### Changed

* Allow to build with fmt 11 ([#97](https://github.com/Simple-Robotics/proxsuite-nlp/pull/97))

## [0.6.1] - 2024-05-13

### Changed

* Changes to includes and tests for linesearch methods ([#81](https://github.com/Simple-Robotics/proxsuite-nlp/pull/81))
* Solver: store problem instance as a raw pointer, change solver ctor ([#79](https://github.com/Simple-Robotics/proxsuite-nlp/pull/79))

## [0.6.0] - 2024-05-02

### Added

* Added `ConstraintSetProduct` ([#74](https://github.com/Simple-Robotics/proxsuite-nlp/pull/74))

### Fixed

* Include `<cassert>` in `math.hpp` to fix possible compilation issues ([#77](https://github.com/Simple-Robotics/proxsuite-nlp/pull/77))

### Changed

* `EqualityConstraint`/`NegativeOrthant` template classes changed to `EqualityConstraintTpl`/`NegativeOrthantTpl`
* Deprecate getters `getWorkspace()` and `getResults()` in both C++ and Python ([#76](https://github.com/Simple-Robotics/proxsuite-nlp/pull/76))
* Bump minimum version of eigenpy to 3.4.0 ([#76](https://github.com/Simple-Robotics/proxsuite-nlp/pull/76))

## [0.5.0] - 2024-04-23

### Fixed

* Enhance CMake packaging ([165](https://github.com/Simple-Robotics/proxsuite-nlp/pull/65))

## [0.4.0] - 2024-01-31

### Fixed

* Add missing dependencies in `package.xml`: pinocchio, eigen.
* Fix `ConstraintObjectTpl::operator==` constness (mandatory for eigenpy 3.3)
* Corner case in `BunchKaufman<>` decomposition class when number of lhs rows is 1
* Memory allocation in `BunchKaufman<>` ([#66](https://github.com/Simple-Robotics/proxsuite-nlp/pull/66))

### Added

* Typedef for `Scalar` in the matrix decomposition classes
* `.solve(rhs)` (allocating version of `.solveInPlace()`) to their C++ class and Python bindings

## [0.3.4] - 2024-01-19

### Fixed

* Missing installation of template declaration header `modelling/constraints.txx`

## [0.3.3] - 2024-01-19

### Fixed

* Don't use virtual inheritance to implement `finite_difference_wrapper`
* Build on Windows
* Fix Armijo lineseach exit condition

## [0.3.2] - 2024-01-12

### Changed

* Changed the minimum version of eigenpy to 3.2.0

## [0.3.1] - 2023-12-21

### Fixed

* Fixed a missing `#pragma once` in `linalg/bunchkaufman.hpp`
* Fix benchmarks build with MacOS
* Fix pkg-config definitions

## [0.3.0] - 2023-12-19

### Added

* This is the first release of `proxsuite-nlp`. This library is a joint effort between LAAS-CNRS and INRIA, and will be maintained and expanded in the future. Please provide constructive feedback and contribute!

[Unreleased]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.7.1...HEAD
[0.7.1]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.6.1...v0.7.0
[0.6.1]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.3.4...v0.4.0
[0.3.4]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.3.3...v0.3.4
[0.3.3]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.3.2...v0.3.3
[0.3.2]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/Simple-Robotics/proxsuite-nlp/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/Simple-Robotics/proxsuite-nlp/releases/tag/v0.3.0
