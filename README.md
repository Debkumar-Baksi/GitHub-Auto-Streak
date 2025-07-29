# Git Streak Tracker 📱

A beautiful and modern Android app built with Kivy to help you track your daily coding streak by automatically logging and pushing to your GitHub repository.

![Git Streak Tracker](https://img.shields.io/badge/Version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-green.svg)
![Kivy](https://img.shields.io/badge/Kivy-2.0+-orange.svg)
![Android](https://img.shields.io/badge/Android-5.0+-red.svg)

## ✨ Features

- **🎨 Beautiful Modern UI/UX**: Clean, intuitive interface with smooth animations
- **🔒 Error-Free Git Operations**: Robust error handling and validation
- **⚡ Background Processing**: Non-blocking operations for better user experience
- **📊 Real-time Status Updates**: Live feedback on all operations
- **📝 Custom Commit Messages**: Personalize your streak entries
- **🔗 Repository Management**: Save and manage multiple repositories
- **📱 Recent Log Display**: View your recent streak entries
- **🌐 URL Validation**: Smart GitHub URL validation
- **💾 Offline Logging**: Track streaks even without internet

## 🚀 Quick Start

### Prerequisites

- Android 5.0 (API level 21) or higher
- Internet connection for git operations
- GitHub repository access

### Installation

1. **Download the APK**:
   - Go to the [Releases](https://github.com/yourusername/git-streak-tracker/releases) page
   - Download the latest APK file

2. **Install on Android**:
   - Enable "Install from Unknown Sources" in your Android settings
   - Install the downloaded APK file
   - Open the app

3. **Set up your repository**:
   - Enter your GitHub repository URL (e.g., `https://github.com/username/repository`)
   - The app will save this for future use
   - Start tracking your coding streak!

## 📖 Usage Guide

### First Time Setup

1. **Enter Repository URL**: 
   - Paste your GitHub repository URL in the first field
   - The app validates the URL format automatically
   - Valid URLs will show a green checkmark

2. **Optional Commit Message**:
   - Enter a custom commit message (optional)
   - If left empty, a default message with timestamp will be used

3. **Log Your Streak**:
   - Tap "📝 Log & Push to GitHub"
   - The app will automatically:
     - Initialize git repository (if needed)
     - Create/update log.txt file
     - Add and commit changes
     - Push to your GitHub repository

### Daily Usage

1. **Quick Log**: Just tap the "📝 Log & Push to GitHub" button
2. **Custom Message**: Add a personal message about your coding session
3. **View History**: Check the "Recent Log Entries" section to see your streak

### Managing Repositories

- **Save Repository**: First-time use automatically saves the repository URL
- **Clear Saved Repo**: Use the "🗑️ Clear Saved Repo" button to remove saved repository
- **Switch Repositories**: Clear the saved repo and enter a new URL

## 🛠️ Development

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/git-streak-tracker.git
   cd git-streak-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install kivy
   ```

3. **Run the app**:
   ```bash
   python main.py
   ```

### Building APK Locally

1. **Install Buildozer**:
   ```bash
   pip install buildozer
   ```

2. **Initialize Buildozer** (if needed):
   ```bash
   buildozer init
   ```

3. **Build APK**:
   ```bash
   buildozer android debug
   ```

### GitHub Actions Build

The project includes GitHub Actions workflow that automatically builds APK on every push to main/master branch:

- **Automatic Build**: Pushes to main/master trigger APK build
- **Release Creation**: Successful builds create GitHub releases
- **Artifact Upload**: APK files are uploaded as artifacts

## 🏗️ Architecture

### Key Components

- **Main App Class**: `GitStreakMain` - Entry point of the application
- **UI Layout**: `GitStreakApp` - Main UI container with beautiful design
- **Custom Widgets**: Custom styled buttons, inputs, and labels
- **Background Processing**: Threading for non-blocking git operations
- **Error Handling**: Comprehensive error handling and user feedback

### File Structure

```
git-streak-tracker/
├── main.py                 # Main application code
├── buildozer.spec          # Buildozer configuration
├── .github/
│   └── workflows/
│       └── build-apk.yml   # GitHub Actions workflow
├── README.md              # This file
├── log.txt                # Streak log file (auto-generated)
└── .primary_repo.txt      # Saved repository URL (auto-generated)
```

## 🔧 Configuration

### Buildozer Settings

The `buildozer.spec` file is configured for optimal Android builds:

- **Target API**: Android 13 (API 33)
- **Minimum API**: Android 5.0 (API 21)
- **Architectures**: arm64-v8a, armeabi-v7a
- **Permissions**: Internet, Storage, Network State
- **Theme**: NoTitleBar for full-screen experience

### Customization

You can customize the app by modifying:

- **Colors**: Update the KV string in `main.py`
- **Permissions**: Modify `android.permissions` in `buildozer.spec`
- **App Info**: Change title, package name, and version in `buildozer.spec`

## 🐛 Troubleshooting

### Common Issues

1. **Git Authentication Error**:
   - Ensure your repository is public or you have proper access
   - Check your GitHub credentials

2. **Network Connection Error**:
   - Verify internet connection
   - Check if GitHub is accessible

3. **Permission Denied**:
   - Grant storage permissions to the app
   - Enable "Install from Unknown Sources" for APK installation

4. **Build Failures**:
   - Check buildozer.spec configuration
   - Ensure all dependencies are installed
   - Verify Android SDK setup

### Debug Mode

Enable debug logging by setting `log_level = 2` in `buildozer.spec`:

```ini
[buildozer]
log_level = 2
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kivy Team**: For the amazing cross-platform framework
- **Buildozer**: For simplifying Android builds
- **GitHub Actions**: For automated CI/CD pipeline

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/git-streak-tracker/issues) page
2. Create a new issue with detailed description
3. Include device information and error logs

## 🔄 Changelog

### Version 1.0.0
- ✨ Initial release with beautiful UI/UX
- 🔒 Error-free git operations
- ⚡ Background processing
- 📊 Real-time status updates
- 📝 Custom commit messages
- 🔗 Repository management
- 📱 Recent log display

---

**Made with ❤️ for the coding community** 