import os
import subprocess
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class GitStreakApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.repo_url_input = TextInput(hint_text="Paste your GitHub repo URL (e.g. https://github.com/user/repo.git)", multiline=False)
        self.add_widget(self.repo_url_input)

        self.commit_msg_input = TextInput(hint_text="Enter your commit message", multiline=False)
        self.add_widget(self.commit_msg_input)

        self.status_label = Label(text="Status: Waiting for input...")
        self.add_widget(self.status_label)

        self.commit_btn = Button(text="Initialize & Commit to GitHub")
        self.commit_btn.bind(on_press=self.handle_commit)
        self.add_widget(self.commit_btn)

    def handle_commit(self, instance):
        repo_url = self.repo_url_input.text.strip()
        commit_msg = self.commit_msg_input.text.strip()

        if not repo_url:
            self.status_label.text = "❌ Error: GitHub URL required"
            return

        if not commit_msg:
            commit_msg = f"Auto commit at {datetime.now()}"

        try:
            if not os.path.exists("log.txt"):
                with open("log.txt", "w") as f:
                    f.write(f"{datetime.now()} - {commit_msg}\n")
            else:
                with open("log.txt", "a") as f:
                    f.write(f"{datetime.now()} - {commit_msg}\n")

            # Git setup
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "remote", "remove", "origin"], check=False)  # just in case
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "branch", "-M", "main"], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

            self.status_label.text = "✅ Successfully pushed to GitHub!"

        except subprocess.CalledProcessError as e:
            self.status_label.text = f"❌ Git Error: {e}"


class GitStreakMain(App):
    def build(self):
        return GitStreakApp()


if __name__ == "__main__":
    GitStreakMain().run()
