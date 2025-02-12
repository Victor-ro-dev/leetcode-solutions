"""
Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números de modo que a soma deles sejatarget .

Você pode assumir que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tamanho = len(nums)
        
        for i in range(tamanho):  # Primeiro número
            for j in range(i + 1, tamanho):  # Segundo número
                if nums[i] + nums[j] == target:
                    return [i, j]  # Retorna os índices encontrados