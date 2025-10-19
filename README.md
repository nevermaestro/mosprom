# mosprom
Run the application:   
```sh
git clone https://github.com/nevermaestro/mosprom
cd mosprom/app
python3 -m venv .env
. .env/bin/activate
pip3 install -r requirements.txt
flask --app app run --host=0.0.0.0 --debug
```