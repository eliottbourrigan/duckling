### Quickstart

To create and get access to the VM:

```bash
# Create the VM
az vm create `
    --resource-group ducklings-group `
    --name duckling2 `
    --image Debian11 `
    --size Standard_B1s `
    --admin-username myadmin `
    --admin-password dcA9X77y2DG8pw `
    --public-ip-sku Standard `
    --authentication-type password `
    --no-wait

# Open port 80
az vm open-port --port 80 --resource-group ducklings-group --name duckling2

# Get the public IP
az vm show -d -g ducklings-group -n duckling2 --query publicIps -o tsv

# SSH into the VM
ssh myadmin@4.212.10.34
```

Once on the VM: 

```bash
# Update and upgrade the system
apt-get update
apt-get upgrade -y

# Install Git & Docker
sudo apt install git -y
sudo curl -fsSL get.docker.com | bash

# Clone Duckling
git clone https://github.com/eliottbourrigan/duckling
cd duckling

# Build and run the container
sudo docker build -t duckling .
sudo docker run -p 80:80 duckling
```
