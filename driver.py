import requests
import os
import json
import mimetypes
from typing import Tuple, Optional

class GDrive:
    def __init__(self, ACCESS_TOKEN: str):
        """
        Initializes GDrive instance with the provided access token.
        visit : https://developers.google.com/oauthplayground/#:~:text=Manager%20API%20v2-,Drive%20API%20v3,-Drive%20Activity%20API 
                   or 
                https://developers.google.com/oauthplayground/
        to generate access token.
        Args:
            ACCESS_TOKEN (str): The Google Drive access token.
        """
        headers = {
            "authorization": f"Bearer {ACCESS_TOKEN}",
        }
        self.headers = headers

    def download_file(self, file_id: str, file_name: str) -> Tuple[requests.Response, Optional[str]]:
        """
        Downloads a file from Google Drive.

        Args:
            file_id (str): The ID of the file to download.
            file_name (str): The name to save the downloaded file as.

        Returns:
            Tuple[requests.Response, Optional[str]]: A tuple containing the response and the local file path,
            or (response, None) if download failed.
        """
        try:
            response = requests.get(
                f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media",
                headers=self.headers
            )
            if response.status_code == 200:
                file_path = os.path.join(os.getcwd(), file_name)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                return response, file_path
            else:
                return response, None
        except Exception as e:
            return e, None

    def upload_file(self, file_name: str, file_path: str, drive_folder_id: str = "root") -> requests.Response:
        """
        Uploads a file to Google Drive.

        Args:
            file_name (str): The name to save the uploaded file as.
            file_path (str): The local path of the file to upload.
            drive_folder_id (str): The ID of the Google Drive folder to upload the file to.

        Returns:
            requests.Response: The response from the upload request.
        """
        try:
            params = {
                "name": file_name,
                "parents": [drive_folder_id]
            }
            if not os.path.exists(file_path):
                raise Exception("File not found")
            file_type = mimetypes.guess_type(file_path)[0]
            files = {
                'data': ('metadata', json.dumps(params), 'application/json;charset=UTF-8'),
                'file': (file_name, open(file_path, 'rb'), file_type)
            }
            res = requests.post(
                'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart',
                headers=self.headers,
                files=files
            )
            return res
        except Exception as e:
            return e

    def delete_file(self, file_id: str) -> requests.Response:
        """
        Deletes a file from Google Drive.

        Args:
            file_id (str): The ID of the file to delete.

        Returns:
            requests.Response: The response from the delete request.
        """
        response = requests.delete(
            f"https://www.googleapis.com/drive/v3/files/{file_id}",
            headers=self.headers
        )
        return response

    def create_folder(self, folder_name: str, parent_folder_id: str = "root") -> requests.Response:
        """
        Creates a folder in Google Drive.

        Args:
            folder_name (str): The name of the folder to create.
            parent_folder_id (str): The ID of the parent folder.

        Returns:
            requests.Response: The response from the create folder request.
        """
        folder_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_folder_id]
        }

        response = requests.post(
            "https://www.googleapis.com/drive/v3/files",
            headers=self.headers,
            data=json.dumps(folder_metadata)
        )
        return response

    def delete_folder(self, folder_id: str) -> requests.Response:
        """
        Deletes a folder from Google Drive.

        Args:
            folder_id (str): The ID of the folder to delete.

        Returns:
            requests.Response: The response from the delete folder request.
        """
        headers = self.headers.copy()
        headers["Content-Type"] = "application/json"
        response = requests.delete(
            f"https://www.googleapis.com/drive/v3/files/{folder_id}",
            headers=headers
        )
        return response

    def search_file(self, file_name: str) -> requests.Response:
        """
        Searches for a file in Google Drive.

        Args:
            file_name (str): The name of the file to search for.

        Returns:
            requests.Response: The response from the file search request.
        """
        response = requests.get(
            "https://www.googleapis.com/drive/v3/files",
            headers=self.headers,
            params={"q": f"name='{file_name}'"}
        )
        return response


if __name__ == "__main__":
    # Example usage
    gdrive = GDrive("<ACCESS_TOKEN>")

    # Upload file
    res = gdrive.upload_file("file_name.png", "/path/to/file.png")
    print(res.json())
    print('\n')

    # Search for a file
    res = gdrive.search_file("file_name.png")
    print(res.json())
    print('\n')



    # Download a file
    res, file_path = gdrive.download_file("<file_id>", "/path/to/file.png")
    print(res, file_path)
    print('\n')
    
    
    # Delete a file
    res = gdrive.delete_file("<file_id>")
    print(res.json())
    print('\n')

    # Create a folder
    res = gdrive.create_folder("<folder_name>")
    print(res.json())
    print('\n')
    # Delete a folder
    res = gdrive.delete_folder("<folder_id>")
    print(res)
