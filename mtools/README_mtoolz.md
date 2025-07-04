# mtoolz - Enhanced MongoDB Diagnostic Tools

Enhanced version of mtools with **MongoDB 4.4+ JSON log format support**.

## 🚀 Quick Installation

### Option 1: One-liner installation
```bash
curl -sSL https://raw.githubusercontent.com/jenunes/mtoolz/main/mtools/install_mtoolz.sh | bash
```

### Option 2: Manual installation
```bash
# Clone the repository
git clone https://github.com/jenunes/mtoolz.git
cd mtoolz

# Install in development mode
pip install -e .
```

### Option 3: Direct install from GitHub
```bash
pip install git+https://github.com/jenunes/mtoolz.git
```

## 🎯 What's New in mtoolz

- ✅ **MongoDB 4.4+ JSON Log Support**: Parse the new JSON log format
- ✅ **Enhanced Connection Analysis**: Full connection statistics for JSON logs
- ✅ **Fixed Import Issues**: All import paths updated for standalone usage
- ✅ **Better Error Handling**: Improved compatibility across MongoDB versions

## 📊 Usage Examples

### Basic Log Analysis
```bash
# Analyze MongoDB 4.4+ JSON logs
mloginfo /path/to/mongodb.log

# Connection analysis (now works with JSON logs!)
mloginfo /path/to/mongodb.log --connections

# Connection statistics with duration analysis
mloginfo /path/to/mongodb.log --connstats

# Restart information
mloginfo /path/to/mongodb.log --restarts
```

## 🔧 Supported MongoDB Versions

- **Legacy Format**: MongoDB 4.0 and older
- **JSON Format**: MongoDB 4.4+ (new!)

## 📈 Connection Analysis Features

With JSON log support, you can now analyze:
- Total connections opened/closed
- Connection duration statistics (min/max/average)
- IP-based connection analysis
- Socket exception tracking

## 📖 More Information

- **Repository**: https://github.com/jenunes/mtoolz
- **Original mtools**: https://github.com/rueckstiess/mtools

---

**mtoolz v8.0.0** - Enhanced MongoDB diagnostic tools with JSON log support
