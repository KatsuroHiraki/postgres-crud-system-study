## Architecture Refactoring & Repository Pattern
- **Learned:** Separation of Concerns, Repository Pattern for DB access, Context Managers for connection safety, dataclass models, and environment variable management using `.env`.
- **Built:**
  - connection.py: Context-managed database cursor layer.
  - repositories.py: Product repository executing clean object-relational mapping.
  - main.py: Enterprise-structured execution entry point detached from direct SQL queries.