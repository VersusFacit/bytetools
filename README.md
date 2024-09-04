# bytetools

## 🚧 ACTIVELY UNDER CONSTRUCTION

`bytetools` was born out of frustration with the limited functionality provided by Python's `bytearray` and `bytes` types while writing a `is_pallindrome` function on `bytearray`s.

While these built-in types are useful, they often lack the features needed for more advanced byte manipulation. This library is intended to fill that gap by providing a set of tools and educational utilities for byte-level operations.

In addition to its practical applications, `bytetools` can also serve as a utility or "glue" in various contexts where byte-level operations are required.

## Features

- **High-Performance Byte Manipulation**: Core byte operations, such as `lower()` to convert individual ASCII bytes to their lowercase counterparts, are implemented in C to deliver optimal performance and the educational utility from the exercise itself.
- **Custom Exceptions**: Includes built-in custom exceptions like `InvalidByteValue` for clear, robust error handling during byte operations.
- **Seamless Python Integration**: Written in C but designed to be seamlessly used as a Python package, with transparent installation via `pip`.

## Installation

You can install `bytetools` directly from PyPI using `pip`:

```bash
pip install bytetools
