Sub CheckHyperlinks()
    Dim ws As Worksheet
    Dim rng As Range
    Dim cell As Range
    Dim hyperlinkAddress As String
    
    ' 対象となるシートを指定します
    Set ws = ThisWorkbook.Sheets("Sheet1") ' シート名を変更してください
    
    ' シート内のすべてのセルを対象にします
    Set rng = ws.UsedRange
    
    ' 各セルに対してハイパーリンクをチェックします
    For Each cell In rng
        If cell.Hyperlinks.Count > 0 Then
            ' ハイパーリンクが存在する場合、アドレスを取得します
            hyperlinkAddress = cell.Hyperlinks(1).Address
            
            ' リンクがフォルダの場合
            If IsFolder(hyperlinkAddress) Then
                ' フォルダが存在しない場合、セルの色を赤色にします
                If Not FolderExists(hyperlinkAddress) Then
                    cell.Font.Color = RGB(255, 0, 0) ' 赤色
                End If
            ' リンクがファイルの場合
            ElseIf Not FileExists(hyperlinkAddress) Then
                ' ファイルが存在しない場合、セルの色を赤色にします
                cell.Font.Color = RGB(255, 0, 0) ' 赤色
            End If
        End If
    Next cell
End Sub

Function IsFolder(path As String) As Boolean
    ' パスがフォルダであるかどうかを判定します
    IsFolder = GetAttr(path) And vbDirectory
End Function

Function FolderExists(folderPath As String) As Boolean
    ' フォルダが存在するかどうかを確認します
    If Dir(folderPath, vbDirectory) <> "" Then
        FolderExists = True
    Else
        FolderExists = False
    End If
End Function