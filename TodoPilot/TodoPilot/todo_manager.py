import json
import uuid
from datetime import datetime
import os

class TodoManager:
    def __init__(self, data_file="tasks.json"):
        """Initialize the TodoManager with a data file for persistence."""
        self.data_file = data_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            return []
    
    def _save_tasks(self):
        """Save tasks to the JSON file."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            return True
        except IOError as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def add_task(self, description):
        """Add a new task with the given description."""
        if not description or not description.strip():
            return False
        
        task = {
            'id': str(uuid.uuid4()),
            'description': description.strip(),
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed_at': None
        }
        
        self.tasks.append(task)
        return self._save_tasks()
    
    def delete_task(self, task_id):
        """Delete a task by its ID."""
        original_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        
        if len(self.tasks) < original_length:
            return self._save_tasks()
        return False
    
    def toggle_task_completion(self, task_id):
        """Toggle the completion status of a task."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                if task['completed']:
                    task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                else:
                    task['completed_at'] = None
                return self._save_tasks()
        return False
    
    def get_all_tasks(self):
        """Get all tasks."""
        return self.tasks.copy()
    
    def get_filtered_tasks(self, filter_type="all"):
        """Get tasks filtered by type (all, active, completed)."""
        if filter_type == "active":
            return [task for task in self.tasks if not task['completed']]
        elif filter_type == "completed":
            return [task for task in self.tasks if task['completed']]
        else:  # all
            return self.tasks.copy()
    
    def get_task_by_id(self, task_id):
        """Get a specific task by its ID."""
        for task in self.tasks:
            if task['id'] == task_id:
                return task.copy()
        return None
    
    def update_task_description(self, task_id, new_description):
        """Update the description of a task."""
        if not new_description or not new_description.strip():
            return False
        
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description.strip()
                return self._save_tasks()
        return False
    
    def get_task_statistics(self):
        """Get statistics about tasks."""
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task['completed']])
        active = total - completed
        
        return {
            'total': total,
            'completed': completed,
            'active': active
        }
