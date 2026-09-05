# Handoff Specification

Every work unit must end with the following fields, even when blocked:

- branch;
- commit base;
- commits produced;
- primary-session model and effort actually used;
- every agent actor, primary/subagent status, functional role, exact model, effort, and routing rationale;
- model reassignments, escalations, equivalent-tier mappings, and routing deviations, or an explicit `none`;
- objective and completion verdict;
- deliverables and primary files;
- sources added;
- coverage reached;
- validations executed and results;
- gaps;
- divergences;
- provisional information;
- explicitly unperformed work;
- error-log path, resolved event IDs, and open event IDs;
- human-review question path and gate consequences;
- recommended next bounded work unit, without starting it.

For integration handoffs, also record merged branches, merge commits, conflict resolutions, global indexes updated, final validation, and remote synchronization state. Integration, final audit, and global synthesis must be performed directly by the user-supervised primary session at its active model/effort; they must never be delegated to a Sol subagent.
