import streamlit as st
import json
import uuid
from datetime import datetime
from todo_manager import TodoManager

# Initialize the todo manager
@st.cache_resource
def get_todo_manager():
    return TodoManager()

def main():
    st.title("📋 To-Do List Application")
    st.markdown("---")
    
    # Initialize todo manager
    todo_manager = get_todo_manager()
    
    # Sidebar for adding new tasks
    with st.sidebar:
        st.header("➕ Add New Task")
        
        # Task input form
        with st.form("add_task_form"):
            task_description = st.text_area(
                "Task Description",
                placeholder="Enter your task description here...",
                height=100
            )
            
            submitted = st.form_submit_button("Add Task", use_container_width=True)
            
            if submitted:
                if task_description.strip():
                    success = todo_manager.add_task(task_description.strip())
                    if success:
                        st.success("Task added successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to add task. Please try again.")
                else:
                    st.error("Please enter a task description.")
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.header("📝 Tasks")
    
    with col2:
        # Filter options
        filter_option = st.selectbox(
            "Filter",
            ["All", "Active", "Completed"],
            key="filter_select"
        )
    
    # Get filtered tasks
    tasks = todo_manager.get_filtered_tasks(filter_option.lower())
    
    # Display tasks
    if not tasks:
        if filter_option == "All":
            st.info("🎉 No tasks yet! Add your first task using the sidebar.")
        elif filter_option == "Active":
            st.info("✨ No active tasks! All tasks are completed.")
        else:
            st.info("📭 No completed tasks yet.")
    else:
        # Task statistics
        total_tasks = len(todo_manager.get_all_tasks())
        completed_tasks = len([t for t in todo_manager.get_all_tasks() if t['completed']])
        active_tasks = total_tasks - completed_tasks
        
        st.markdown(f"""
        **Task Statistics:** 
        Total: {total_tasks} | Active: {active_tasks} | Completed: {completed_tasks}
        """)
        
        st.markdown("---")
        
        # Display each task
        for task in tasks:
            with st.container():
                col1, col2, col3 = st.columns([6, 1, 1])
                
                with col1:
                    # Task description with completion status
                    if task['completed']:
                        st.markdown(f"~~{task['description']}~~")
                        st.caption(f"✅ Completed on: {task['completed_at']}")
                    else:
                        st.markdown(f"**{task['description']}**")
                        st.caption(f"📅 Created on: {task['created_at']}")
                
                with col2:
                    # Toggle completion button
                    if task['completed']:
                        if st.button("↩️", key=f"uncomplete_{task['id']}", help="Mark as incomplete"):
                            todo_manager.toggle_task_completion(task['id'])
                            st.rerun()
                    else:
                        if st.button("✅", key=f"complete_{task['id']}", help="Mark as complete"):
                            todo_manager.toggle_task_completion(task['id'])
                            st.rerun()
                
                with col3:
                    # Delete button
                    if st.button("🗑️", key=f"delete_{task['id']}", help="Delete task"):
                        todo_manager.delete_task(task['id'])
                        st.rerun()
                
                st.markdown("---")
    
    # Footer with additional information
    st.markdown("---")
    st.markdown(
        "💡 **Tips:** Use the sidebar to add new tasks. Click ✅ to mark tasks as complete, "
        "↩️ to mark them as incomplete, and 🗑️ to delete them."
    )

if __name__ == "__main__":
    main()
