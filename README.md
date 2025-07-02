# DomainEditor
Official Level Editor of Domain Echoing

## Build
```bash
pyinstaller --windowed --name SpectrumEditor main.py
````

### 安装
```bash
pip install pyinstaller
````

### 打包 GUI 应用（无终端）
```bash
pyinstaller --windowed --onefile --name SpectrumEditor main.py
```

### 可选：添加图标
```bash
pyinstaller --windowed --onefile --icon=icon.ico --name SpectrumEditor main.py
```