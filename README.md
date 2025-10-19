# MosProm Hackathon 
> Raw and unfinished yet so pure and full of joy!
## Run the application
### scripts
First you must clone the repository.
```sh
git clone https://github.com/nevermaestro/mosprom
cd mosprom
```
Then run the provided setup script:
```sh
chmod +x setup.sh run.sh && ./setup.sh
```
You can now use the run script to run the application:
```sh
./run.sh
```
Advanced users may wish to edit these files themselves or take a more straightforward approach.
### shell
First you must clone the repository:
```sh
git clone https://github.com/nevermaestro/mosprom
cd mosprom/app
```
Setup the virtual environment:
```sh
python3 -m venv .env
. .env/bin/activate
```
Install the necessary requirements:
```sh
pip install -r requirements.txt
```
Run the application:
```sh
flask --app app run --host=0.0.0.0 --debug
```
