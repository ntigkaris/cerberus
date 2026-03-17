# Documentation

### What is cerberus?

Cerberus is a Python-based security solution developed for *Windows Vista* and subsequent OS versions. It periodically keeps activity records by taking snapshots during user sessions. Its core functionality includes recording the contents of the user’s *Home* directory and capturing a *photo* of the individual operating the computer at one-hour intervals. This mechanism provides an additional layer of monitoring for machines that are not protected by user authentication or that are accessible in shared and public environments.

### How to install

### What makes cerberus truly lightweight?

### Configuration

The following parameters are available for customization, allowing users to tailor the system behavior to their specific requirements:

| Parameters | Description |
| --- | --- |
| filename | defines the naming convention for generated files. In our implementation we use the following datetime format *"YYYYmmddHH24MMSS"* |
| cleanup | specifies the retention period (days). The system scans configured directories and archives content within this threshold |
| imgdir | indicates the directory where captured photographs are stored |
| recdir | indicates the directory where Home directory logs are stored |
| tmpdir | specifies the directory utilized by the *cleanUp* function |
| rectype | sets the file extension for Home directory logs |
| imgtype | sets the file extension for captured photographs |
| imgsize | determines the captured photograph's resolution |
| kernel | configures the image transformation kernel applied |

For frequent users, we recommend the following setup:

| Parameter | Value |
| --- | --- |
| cleanup | 7 |
| imgtype | jpg |
| imgsize | 256 |

For users logging into their devices sparingly, we instead suggest using:

| Parameter | Value |
| --- | --- |
| cleanup | 30 |
| imgtype | jpg |
| imgsize | 512 |

These combinations provide a balance between efficient memory management and output quality, based on usage patterns.

### Modules

Throughout the development process, native Python standard library modules **os**, **datetime**, **pathlib** and **shutil** are utilized to ensure portability and minimal external dependencies.

- **pywin32**
  
  Here we use the **pywin32** package to access the Windows Task Scheduler API. For more information we provide the following resources:
  1. https://mhammond.github.io/pywin32/
  2. https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-objects

- **cv2**
