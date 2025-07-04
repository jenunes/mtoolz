#!/bin/bash

# mtoolz Installation Script
# Enhanced MongoDB diagnostic tools with MongoDB 4.4+ JSON log support

echo "🚀 Installing mtoolz - Enhanced MongoDB Diagnostic Tools"
echo "========================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    echo "Please install pip3 and try again."
    exit 1
fi

echo "✅ Python 3 and pip3 found"

# Clone the repository
echo "📥 Cloning mtoolz repository..."
if [ -d "mtoolz" ]; then
    echo "📁 mtoolz directory already exists, updating..."
    cd mtoolz
    git pull origin main
else
    git clone https://github.com/jenunes/mtoolz.git
    cd mtoolz
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt 2>/dev/null || echo "⚠️  No requirements.txt found, continuing..."

# Install mtoolz in development mode
echo "🔧 Installing mtoolz..."
pip3 install -e .

echo ""
echo "✅ Installation complete!"
echo ""
echo "🎯 Usage examples:"
echo "  mloginfo /path/to/mongodb.log --connections"
echo "  mloginfo /path/to/mongodb.log --connstats"
echo "  mloginfo /path/to/mongodb.log --restarts"
echo ""
echo "📖 For more information, visit: https://github.com/jenunes/mtoolz"
echo "" 