#!/bin/bash

# Create the main directory if it doesn't exist
mkdir -p brain 

session=1

question="Qual é o teu nome?"

construct_Question() {
   readarray -t duvidas < "brain/Logos/duvidas.txt"
   readarray -t Abs < "brain/Logos/conceitos absolutos.txt"
   readarray -t Rel < "brain/Logos/conceitos relativos.txt"

   local duvida="${duvidas[1]}"
   local relativo="${Rel[1]}" 
   local absoluto="${Abs[3]}"
   # NAO SEI O QUE ESTÁ A ACONTECER AQUI LOL
   echo "$duvida $relativo $absoluto"
}


while true; do
  echo "$question"
  
  if [ "$question" == "Qual é o teu nome?" ]; then 
     # Checkar se a questão a ser feita é a questão é a que permite identificar o usuário
     read nome
      
     # Sanitize input for file name:
     safe_nome=$(basename "$nome" .txt)
     safe_nome="${safe_nome// /_}"  # Replace spaces with underscores
  
     # Construct directory with safe_nome
     directory="brain/${safe_nome}"
  
     # Processamento do nome
     if [ -d "$directory" ]; then #Reconhecimento de um novo nome
       echo "   Olá de volta"
     fi
     if [ ! -d "$directory" ]; then #Conhecimento de um novo nome
       mkdir ${directory} 
     fi


     # Construct session number
     session=$(find "$directory" -type f | wc -l)

     echo "   This is the session ${session}"

     # Construct file name with session number
     filename="${directory}/session${session}.txt"
     answer=$nome
  else 
    #Caso não seja a questão para identificar o usuário, deverá proceder como se fosse uma outra questão (relativa ao usuário em questão) 
     read answer
     if [ "$answer" == "Xau" ]; then
        break
     fi
  fi
  # Construct the string
  date=$(date +%F)
  string="-----------------------------------
  Session $session $date   $nome
  -----------------------------------

  Q\"${question}\"
  R\"${answer}\"
  "

  # Append to file
  echo "$string" >> "$filename"
  question=$(construct_Question)
done
