# Get all .py files in the current directory
$files = Get-ChildItem -Path . -Filter *.py

# Destination directory
$destination = "D:\"

# Remove all py files from the destination
Get-ChildItem -Path $destination -Filter *.py | Remove-Item

# Copy each file to the destination
foreach ($file in $files)
{
    if ($file.Name -eq "main.py")
    {
        $destinationPath = Join-Path -Path $destination -ChildPath "main.py"
    }
    else
    {
        $destinationPath = Join-Path -Path $destination -ChildPath $file.Name
    }
    Copy-Item -Path $file.FullName -Destination $destinationPath
}