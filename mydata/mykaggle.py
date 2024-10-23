import kagglehub

# Download latest version
path = kagglehub.dataset_download(
    "thedevastator/us-baby-names-by-year-of-birth",
    path = 'C:/Users/goper/Files/vsCode/DataRepo/mydata/SSAnames.csv')

print("Path to dataset files:", path)