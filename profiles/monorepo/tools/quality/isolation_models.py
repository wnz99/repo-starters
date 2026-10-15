# SPDX-License-Identifier: CC0-1.0
"""Typed projections of bootstrap inventory and Python package metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from pathlib import Path


class Component(BaseModel):
    model_config = ConfigDict(extra="allow", hide_input_in_errors=True)
    name: str
    path: str
    language: Literal["python", "typescript"]
    import_package: str | None = Field(default=None, alias="importPackage")


class Inventory(BaseModel):
    model_config = ConfigDict(extra="allow", hide_input_in_errors=True)
    baseline: Literal["wnz-repo-v1"]
    runtimes: dict[str, str | None]
    components: list[Component]


class IncludeGroup(BaseModel):
    model_config = ConfigDict(extra="forbid", hide_input_in_errors=True)
    include_group: str = Field(alias="include-group")


class Metadata(BaseModel):
    model_config = ConfigDict(hide_input_in_errors=True)
    name: str
    version: str
    dependencies: list[str] = Field(default_factory=list)
    optional_dependencies: dict[str, list[str]] = Field(
        default_factory=dict, alias="optional-dependencies"
    )


class Manifest(BaseModel):
    model_config = ConfigDict(hide_input_in_errors=True)
    project: Metadata
    groups: dict[str, list[str | IncludeGroup]] = Field(
        default_factory=dict, alias="dependency-groups"
    )


@dataclass(frozen=True)
class Project:
    directory: Path
    manifest: Manifest
