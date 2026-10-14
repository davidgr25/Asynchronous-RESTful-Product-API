Write-Host "--- 1. POST: Crear un nuevo producto ---" -ForegroundColor Cyan
curl.exe -X POST "http://127.0.0.1:8000/api/v1/products/" -H "Content-Type: application/json" -d "{\""sku\"": \""PROD-001\"", \""name\"": \""Mechanical Keyboard\"", \""price\"": 79.99, \""stock\"": 15}"
Write-Host "`n"

Write-Host "--- 2. POST: Error de SKU duplicado ---" -ForegroundColor Cyan
curl.exe -X POST "http://127.0.0.1:8000/api/v1/products/" -H "Content-Type: application/json" -d "{\""sku\"": \""PROD-001\"", \""name\"": \""Duplicate Item\"", \""price\"": 20.00, \""stock\"": 5}"
Write-Host "`n"

Write-Host "--- 3. GET: Listar productos ---" -ForegroundColor Cyan
curl.exe -X GET "http://127.0.0.1:8000/api/v1/products/?skip=0&limit=5&name=Keyboard"
Write-Host "`n"

Write-Host "--- 4. GET: Obtener por ID ---" -ForegroundColor Cyan
curl.exe -X GET "http://127.0.0.1:8000/api/v1/products/1"
Write-Host "`n"

Write-Host "--- 5. PUT: Reemplazo total ---" -ForegroundColor Cyan
curl.exe -X PUT "http://127.0.0.1:8000/api/v1/products/1" -H "Content-Type: application/json" -d "{\""sku\"": \""PROD-001\"", \""name\"": \""RGB Wireless Mechanical Keyboard\"", \""price\"": 89.99, \""stock\"": 10}"
Write-Host "`n"

Write-Host "--- 6. PATCH: Actualizacion parcial ---" -ForegroundColor Cyan
curl.exe -X PATCH "http://127.0.0.1:8000/api/v1/products/1" -H "Content-Type: application/json" -d "{\""price\"": 84.50}"
Write-Host "`n"

Write-Host "--- 7. DELETE: Eliminar producto ---" -ForegroundColor Cyan
curl.exe -X DELETE "http://127.0.0.1:8000/api/v1/products/1" -i
Write-Host "`n"

Write-Host "--- 8. GET: Verificar 404 tras eliminar ---" -ForegroundColor Cyan
curl.exe -X GET "http://127.0.0.1:8000/api/v1/products/1"
Write-Host "`n"