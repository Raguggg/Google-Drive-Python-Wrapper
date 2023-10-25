# Google Drive API Python Wrapper

This is a Python class that provides a convenient wrapper for interacting with the Google Drive API. It includes methods for uploading, downloading, deleting files, creating folders, and searching for files on Google Drive.

## Getting Started

### Prerequisites

To use this wrapper, you need a Google Drive access token. This token has a short expiration period, so this wrapper is best suited for temporary automation tasks.

#### Generating Access Token

1. Go to the [Google OAuth Playground](https://developers.google.com/oauthplayground/#:~:text=Manager%20API%20v2-,Drive%20API%20v3,-Drive%20Activity%20API).
![image](https://github.com/Raguggg/Google-Drive-Python-Wrapper/assets/88898517/618fe0ef-4554-4e35-a23b-2a6e85c5ca47)

2. On the left panel, select "Drive API v3."
![image](https://github.com/Raguggg/Google-Drive-Python-Wrapper/assets/88898517/2a251b5a-18ba-4a3c-8652-9f6765043ea2)

3. In the "Select & authorize APIs" section, find "https://www.googleapis.com/auth/drive" and click on it.

4. Click the "Authorize APIs" button.
![image](https://github.com/Raguggg/Google-Drive-Python-Wrapper/assets/88898517/15a13b51-8e84-4cb9-9c7c-bfc75b8e54af)

6. Follow the prompts to log in and grant access.
![image](https://github.com/Raguggg/Google-Drive-Python-Wrapper/assets/88898517/d679f8ed-dc01-4780-9584-9b6c0a4be698)

7. Click the "Exchange authorization code for tokens" button.

![image](https://github.com/Raguggg/Google-Drive-Python-Wrapper/assets/88898517/536d7fee-5496-470f-afeb-928dc3780e09)

8. You will receive an access token. Copy this token for use with the `GDrive` class.

### Installation

No installation is required. Simply include the `GDrive` class in your Python project.

## Usage

1. **Initialization:**

    ```python
    gdrive = GDrive("<YOUR_ACCESS_TOKEN>")
    ```

2. **Upload a File:**

    ```python
    res = gdrive.upload_file("file_name.png", "/path/to/local/file.png")
    print(res.json())
    ```

3. **Search for a File:**

    ```python
    res = gdrive.search_file("file_name.png")
    print(res.json())
    ```

4. **Download a File:**

    ```python
    res, file_path = gdrive.download_file("<FILE_ID>", "/path/to/save/file.png")
    print(res, file_path)
    ```

5. **Delete a File:**

    ```python
    res = gdrive.delete_file("<FILE_ID>")
    print(res.json())
    ```

6. **Create a Folder:**

    ```python
    res = gdrive.create_folder("<FOLDER_NAME>")
    print(res.json())
    ```

7. **Delete a Folder:**

    ```python
    res = gdrive.delete_folder("<FOLDER_ID>")
    print(res)
    ```

## Note

- Make sure to replace placeholders like `<YOUR_ACCESS_TOKEN>`, `<FILE_ID>`, `<FOLDER_NAME>`, `<FOLDER_ID>` with your actual values.

- The example usage assumes you have a file and folder with the specified names and IDs on your Google Drive.

- This wrapper is designed for temporary automation tasks due to the short expiration period of the access token.

- For Long time use refer here [Dirve automation](https://ragug.medium.com/how-to-upload-files-using-the-google-drive-api-in-python-ebefdfd63eab)

Feel free to customize and integrate these methods into your project as needed.

## Others
<div>
  <a href="https://github.com/raguggg/quillbot-premium-for-free">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=raguggg&theme=highcontrast&repo=quillbot-premium-for-free" />
  </a>
   <a href="https://github.com/Raguggg/colab-as-Vps">
    <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=raguggg&theme=highcontrast&repo=colab-as-Vps" />
  </a>
</div>
<div>
  <span><img align="center" width="400px" height="158px" src="https://github-readme-stats.vercel.app/api?username=raguggg&theme=highcontrast&show_icons=true" /></span>
  <span><img align="center" width="260px" height="158px" src="https://github-readme-stats.vercel.app/api/top-langs/?username=raguggg&theme=highcontrast&layout=compact&langs_count=10" /></span>
</div>



---

> [ragu.great-site.net](http://ragu.great-site.net/) &nbsp;&middot;&nbsp;
> GitHub [@raguggg](https://github.com/raguggg) &nbsp;&middot;&nbsp;
> Instagram [@ragu2k](https://www.instagram.com/ragu2k/)
> Medium [@ragug](https://ragug.medium.com/)
