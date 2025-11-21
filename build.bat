pyinstaller ^
    main.py ^
    -n KovaaKsPlaylistImage ^
    --onefile ^
    --noconsole ^
    --add-data "D:\programming\kovaaks_projects\kovaaks_playlist_image\fonts;fonts/" ^
    --add-data "D:\programming\kovaaks_projects\kovaaks_playlist_image\fonts\Roboto-Bold.ttf;.fonts/Roboto-Bold.ttf" ^
    --add-data "D:\programming\kovaaks_projects\kovaaks_playlist_image\fonts\Roboto-ExtraBold.ttf;.fonts/Roboto-ExtraBold.ttf" ^
    --add-data "D:\programming\kovaaks_projects\kovaaks_playlist_image\fonts\Roboto-Regular.ttf;.fonts/Roboto-Regular.ttf"
