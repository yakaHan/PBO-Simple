# To-Do List Application

## Overview

This is a Streamlit-based to-do list application that provides a simple, web-based interface for task management. The application allows users to add, view, and manage tasks through an intuitive user interface. It uses JSON file storage for data persistence and follows a clean separation of concerns with dedicated modules for UI (Streamlit) and business logic (TodoManager).

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a simple two-tier architecture:

1. **Presentation Layer**: Streamlit-based web interface (`app.py`)
2. **Business Logic Layer**: Task management logic (`todo_manager.py`)
3. **Data Layer**: JSON file-based storage (`tasks.json`)

This architecture was chosen for its simplicity and ease of deployment, making it ideal for a lightweight task management application that doesn't require complex database infrastructure.

## Key Components

### Frontend (app.py)
- **Framework**: Streamlit for rapid web application development
- **UI Components**: 
  - Sidebar form for adding new tasks
  - Main content area for task display and management
  - Column-based layout for organized presentation
- **State Management**: Uses Streamlit's caching mechanism (`@st.cache_resource`) for TodoManager instance

### Backend (todo_manager.py)
- **TodoManager Class**: Core business logic for task operations
- **Task Structure**: Each task contains:
  - Unique UUID identifier
  - Description text
  - Completion status (boolean)
  - Creation timestamp
  - Completion timestamp (nullable)
- **CRUD Operations**: Add, delete, and update task functionality

### Data Storage
- **Format**: JSON file storage for simplicity and portability
- **File**: `tasks.json` stores all task data
- **Persistence**: Automatic save on each operation
- **Error Handling**: Graceful handling of file I/O errors

## Data Flow

1. **Task Creation**: User enters task description → Streamlit form submission → TodoManager.add_task() → JSON file update
2. **Task Display**: Application startup → TodoManager loads from JSON → Streamlit renders UI
3. **Task Operations**: User interactions → TodoManager methods → JSON file persistence → UI refresh

## External Dependencies

### Python Packages
- **Streamlit**: Web application framework for the user interface
- **UUID**: For generating unique task identifiers
- **DateTime**: For timestamp management
- **JSON**: For data serialization and file storage
- **OS**: For file system operations

### Runtime Dependencies
- Python 3.x environment
- Local file system access for JSON storage

## Deployment Strategy

The application is designed for simple deployment scenarios:

1. **Local Development**: Direct Python execution with Streamlit
2. **Replit Environment**: Compatible with Replit's Python runtime
3. **File Storage**: Uses local JSON files, no external database required
4. **Portability**: Self-contained with minimal dependencies

### Deployment Considerations
- **Data Persistence**: Tasks are stored locally in JSON format
- **Scalability**: Current design suitable for single-user scenarios
- **State Management**: Streamlit handles session state and UI updates
- **Error Recovery**: Graceful handling of missing or corrupted data files

### Future Enhancement Opportunities
- Database integration (SQLite, PostgreSQL) for better data management
- Multi-user support with authentication
- Task categorization and filtering
- Due date and priority management
- Export/import functionality