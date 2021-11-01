# Estoque, vendas e metas
estoque = 600
camisetas_vendidas = 500
meta = 500

# A meta foi batida?
meta_batida = camisetas_vendidas == meta
print("A meta de camisas vendidas foi batida")
print(meta_batida)

# Ainda há estoque
estoque_atual = estoque - camisetas_vendidas
em_estoque = estoque_atual != 0
print("Ainda tem camisetas em estoque")
print(em_estoque)