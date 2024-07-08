# Issue RSA private key + public key pair


```shell
# Создайте рядом с папкой нашего проекта папку crets
# путь будет выглядеть так: ./evoll-backend/certs
mkdir certs
```

```shell
# Перейдите в папку
cd certs
```

```shell
# Generate an RSA private key, of size 2048
openssl genrsa -out jwt-private.pem 2048
```

```shell
# Extract the public key from the key pair, which can be used in a certificate
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```

ВАЖНО!\
Добавьте папку и содержимое в .gitignore