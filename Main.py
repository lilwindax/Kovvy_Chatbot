import rasa

config = "config.yml"
training_files = "data/"
domain = "domain.yml"
output = "models/"

model_path = rasa.train(domain, config, [training_files], output)

# rasa run -m models --enable-api --cors "*"