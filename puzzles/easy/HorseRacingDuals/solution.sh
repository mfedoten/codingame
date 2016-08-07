#!/usr/bin/env bash

# This is probably BS, but it works somehow
read N
for (( i=0; i<N; i++ )); do
    read Pi[i]
done

P=( $(
    for i in ${Pi[@]}; do
        echo $i
    done | sort -g ) )


minDif=$((P[1]-P[0])) 

for (( i=1; i<N-1; i++ )); do
    let Ds=$((P[i]-P[i+1]))
    if (( $Ds < 0 ));then
        let Ds=$(( - $Ds))
    fi
    if (( $Ds < $minDif ));then
        let minDif=$Ds
   fi
done

echo $minDif

