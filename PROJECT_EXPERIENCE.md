# Project Experience: Carnage - AI-Powered Voice Assistant

## Project Overview
**Project Name:** Carnage - Intelligent Voice Assistant  
**Role:** Software Developer & ML Engineer  
**Duration:** Personal Project  
**Tech Stack:** Python, PyTorch, OpenAI API, Selenium, NLTK, PyAudio  
**Repository:** https://github.com/amanat-2003/carnage

## Project Description
Developed an advanced AI-powered voice assistant capable of understanding natural language commands and automating various tasks through voice interaction. The system features hands-free operation with clap detection for wake-up functionality and integrates multiple AI models for intelligent conversation and task execution.

## Technical Architecture & Implementation

### 1. Custom Neural Network for Intent Recognition
- **Designed and implemented** a custom PyTorch neural network with 3 fully-connected layers for intent classification
- **Architected** a bag-of-words NLP pipeline using NLTK for tokenization and Porter Stemmer for word normalization
- **Trained** the model on custom dataset with 1000 epochs achieving high accuracy (>75% confidence threshold) for command recognition
- **Optimized** model with Adam optimizer, Cross-Entropy loss function, and batch training (batch size: 8)
- **Implemented** model persistence using PyTorch serialization for efficient loading and inference

### 2. OpenAI API Integration
- **Integrated** OpenAI GPT-3 (text-davinci-002) for conversational AI capabilities
- **Developed** dual-context system:
  - General chat module with temperature=0.5 for natural conversations
  - Q&A module with temperature=0 for factual, precise answers
- **Implemented** conversation logging and context management for maintaining chat history
- **Configured** model parameters (max_tokens, top_p, frequency_penalty, presence_penalty) for optimal response quality

### 3. Audio Processing & Wake-Up System
- **Built** custom clap detection system using PyAudio for hands-free activation
- **Implemented** real-time audio signal processing with RMS (Root Mean Square) calculation
- **Designed** adaptive threshold mechanism to distinguish claps from background noise
- **Developed** voice recognition system for continuous listening and command processing

### 4. Automation & Integration Features
- **Created** modular architecture with separate components for:
  - **Web Automation:** Selenium WebDriver integration for WhatsApp web messaging
  - **Application Launcher:** PyAutoGUI and keyboard automation for launching system applications
  - **Web Browser Control:** Automated website opening and navigation
- **Implemented** intelligent query parsing to extract names, URLs, and application identifiers from natural language
- **Built** cross-platform compatible path handling and system integration

### 5. Code Architecture & Design Patterns
- **Organized** codebase into modular structure:
  - `Brain/` - AI and NLP processing modules
  - `Body/` - Audio I/O (listening and speaking)
  - `Features/` - Task automation modules
  - `Database/` - Persistent storage for logs and model weights
  - `Data/` - Configuration and training data
- **Implemented** clean separation of concerns with dedicated modules for each functionality
- **Designed** extensible architecture allowing easy addition of new commands and features

## Key Features Implemented

### Voice-Controlled Task Automation
- Email composition and sending
- WhatsApp message sending via web automation
- Music playback control
- Wikipedia searches for quick information retrieval
- Web browser control for opening popular websites
- IDE and code editor launching
- IoT device control (Android TV integration)

### Intelligent Conversation
- Context-aware conversational responses
- Question-answering capabilities
- Chat history maintenance
- Fallback mechanism for unrecognized commands

## Technical Skills Demonstrated

### Machine Learning & AI
- Deep learning model design and implementation with PyTorch
- Natural Language Processing (tokenization, stemming, bag-of-words)
- Neural network training and optimization
- Model evaluation and hyperparameter tuning
- Working with pre-trained language models (GPT-3)

### Python Development
- Object-oriented programming and modular design
- Asynchronous programming and event handling
- File I/O and data persistence
- Error handling and exception management
- Package management and dependency handling

### Audio Processing
- Real-time audio stream processing
- Signal processing algorithms (RMS calculation)
- Audio device management and configuration
- Noise filtering and threshold detection

### Web Automation
- Selenium WebDriver implementation
- Browser automation and DOM manipulation
- Session management and cookie handling
- Cross-browser compatibility

### System Integration
- Operating system API interaction
- Keyboard and mouse automation (PyAutoGUI)
- Process control and application launching
- File system operations

## Challenges Overcome

1. **Audio Recognition Accuracy:** Developed adaptive threshold mechanism to handle varying environmental noise levels and prevent false activations

2. **Model Optimization:** Fine-tuned neural network architecture and training parameters to achieve reliable intent classification while preventing overfitting

3. **Context Management:** Implemented persistent chat logging system to maintain conversation context across sessions

4. **Cross-Platform Compatibility:** Designed path handling and system commands to work across different operating systems

5. **Real-time Processing:** Optimized audio processing pipeline to ensure responsive voice command recognition

## Impact & Results

- Created a fully functional hands-free AI assistant with multiple automation capabilities
- Achieved reliable voice command recognition with >75% confidence threshold
- Implemented seamless integration with third-party services (OpenAI, WhatsApp Web)
- Demonstrated strong understanding of ML/AI, NLP, and software architecture principles
- Built extensible system that can be easily enhanced with additional features

## Technical Metrics

- **Model Training:** 1000 epochs with CrossEntropyLoss optimization
- **Audio Processing:** 44.1kHz sample rate, real-time processing
- **Response Time:** Near-instantaneous command execution
- **Model Size:** Lightweight neural network suitable for local deployment
- **Confidence Threshold:** 75% for intent classification

## Future Enhancements (Demonstrating Forward Thinking)

- Multi-user voice recognition and personalization
- Integration with smart home IoT devices
- Offline mode with local language models
- Multi-language support
- Enhanced security with voice authentication
- Cloud deployment for remote access
- Mobile application for cross-platform usage

---

## Key Takeaways for Resume/Applications

**For Machine Learning Roles:**
- Hands-on experience with PyTorch for custom neural network development
- NLP implementation using NLTK and modern techniques
- Model training, optimization, and deployment
- Integration with state-of-the-art language models (GPT-3)

**For Software Engineering Roles:**
- Strong Python programming with clean, modular architecture
- API integration and third-party service management
- Real-time system development and optimization
- Cross-platform development considerations

**For Full-Stack/Automation Roles:**
- Web automation using Selenium
- System integration and process automation
- Audio processing and signal handling
- End-to-end application development

**Soft Skills Demonstrated:**
- Self-directed learning and problem-solving
- System design and architectural thinking
- Code organization and maintainability
- Technical documentation and communication
