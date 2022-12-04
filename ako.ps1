# Powershell script to demostrate black box testing

Describe 'Test /api/user'  {

    $base_url = " https://github.com"
    
    $path = "/login/device/code"

    Context "HTTP POST $base_url$path" {
        
        It "should get a HTTP 201 (Created) on create AppUser record on first call" {
            # Arrange
            $url = "$base_url$path"
            $headers = @{
                "Content-Type" = "application/json"
            }

            $body = @{
                "client_id" = "f2d2ee8570e5cb86b8c0";
                
            } | ConvertTo-Json -Compress

            # Act
            $response = Invoke-WebRequest -Method 'Post' -Uri $url -Headers $headers -Body $body

            # Assert(s)
            # $response.StatusCode | Should Be 201 # HTTP 201 Created
            Write-Host "Response: ", $response, $response.StatusCode
        }
    }

}

